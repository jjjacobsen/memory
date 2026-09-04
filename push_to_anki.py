#!/usr/bin/env python3
"""Sync from AnkiWeb, mirror the memory vault locally, then sync back.

The vault is the source of truth. This script:
  - syncs the local collection with AnkiWeb before changing notes
  - adds every note in the vault that is not already in Anki
  - tags handled notes with a marker tag so their origin is visible
  - deletes any handled note whose content no longer appears in the vault
  - syncs again so the final collection reaches every device

Editing a note's text in the vault counts as add-new plus delete-old, so the
replaced note starts a fresh review schedule. Removing a line from a vault
file removes the corresponding card.

Usage:
  uv run push_to_anki.py                # mirror the vault and sync
  uv run push_to_anki.py --dry-run      # preview every change, change nothing
  uv run push_to_anki.py --no-sync      # mirror locally, skip AnkiWeb sync
"""

import argparse
import html
import pickle
import sqlite3
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from anki.collection import Collection
from anki.sync import SyncAuth

REPO = Path(__file__).parent
ANKI_DATA = Path.home() / ".local/share/Anki2"
COLLECTION_PATH = ANKI_DATA / "User 1/collection.anki2"
PREFS_PATH = ANKI_DATA / "prefs21.db"
PROFILE_NAME = "User 1"

# notes created or adopted by this script carry this tag, deletions only remove tagged notes
MANAGE_TAG = "memory-vault"

# note-type directory -> (Anki model name, field order used in the vault files)
NOTE_TYPES = {
    "basic": ("Basic", ["Front", "Back"]),
    "keybindings": ("Keybindings", ["Effect", "Binding", "Program"]),
    "linux-sys-admin": ("Linux System Admin", ["Concept", "Meaning"]),
    "prayers": ("Prayers", ["Front", "Back"]),
    "quotes": ("Quotes", ["Name", "Quote"]),
    "us-presidents-detail": ("U.S. Presidents - Detail", ["Name", "Detail", "Extra"]),
    "us-presidents-info": ("U.S. Presidents - Info", ["Number", "Name", "Term", "Party", "State"]),
}

# deck directory name -> Anki deck name
DECK_MAP = {
    "christianity": "Christianity",
    "computer-science": "Computer Science",
    "us-presidents": "U.S. Presidents",
}


# field text is inserted as HTML, match what Anki's importer stores: & < > escaped, quotes left raw
def clean_field(text):
    return html.escape(text.strip(), quote=False)


def data_files(note_type_dir):
    return sorted((REPO / note_type_dir).glob("*/*.txt"))


def deck_key_for(data_file, note_type_dir):
    stem = data_file.stem
    prefix = note_type_dir + "_"
    if not stem.startswith(prefix) or stem == prefix:
        raise SystemExit(f"unexpected filename (expected {prefix}<deck>.txt): {data_file}")
    return stem[len(prefix):]


def vault_rows(note_type_dir, field_names):
    # returns row-key -> deck name, so each note is added to its family deck
    rows = {}
    for data_file in data_files(note_type_dir):
        deck_name = DECK_MAP[deck_key_for(data_file, note_type_dir)]
        for line in data_file.read_text().splitlines():
            if not line.strip():
                continue
            values = line.split("|")
            if len(values) != len(field_names):
                raise SystemExit(f"expected {len(field_names)} fields, got {len(values)} in {data_file}:\n{line}")
            rows[tuple(clean_field(v) for v in values)] = deck_name
    return rows


def mirror_model(col, nt_dir, model_name, field_names, dry_run):
    model = col.models.by_name(model_name)
    if model is None:
        raise SystemExit(f"Anki model not found: {model_name}")
    rows = vault_rows(nt_dir, field_names)

    existing = [col.get_note(i) for i in col.find_notes(f'note:"{model_name}"', order=False)]
    present_content = {tuple(n[name] for name in field_names) for n in existing}

    added = tagged = deleted = 0

    # 1. add notes that are in the vault but not in Anki, in their family deck
    for row, deck_name in sorted(rows.items()):
        if row in present_content:
            continue
        if dry_run:
            print(f"would add [{model_name}] {row[0][:60]}")
            continue
        deck = col.decks.by_name(deck_name)
        deck_id = deck["id"] if deck else col.decks.add_normal_deck_with_name(deck_name).id
        note = col.new_note(model)
        for name, value in zip(field_names, row):
            note[name] = value
        note.add_tag(MANAGE_TAG)
        col.add_note(note, deck_id)
        added += 1
        present_content.add(row)

    # 2. tag existing notes that match the vault, so they are managed from now on
    for n in existing:
        if tuple(n[name] for name in field_names) in rows and MANAGE_TAG not in n.tags:
            if dry_run:
                print(f"would tag [{model_name}] {n[field_names[0]][:40]}")
                tagged += 1
                continue
            n.add_tag(MANAGE_TAG)
            col.update_note(n)
            tagged += 1

    # 3. delete notes this script manages whose content is no longer in the vault
    for n in existing:
        if MANAGE_TAG in n.tags and tuple(n[name] for name in field_names) not in rows:
            if dry_run:
                print(f"would delete [{model_name}] {n[field_names[0]][:60]}")
                deleted += 1
                continue
            col.remove_notes([n.id])
            deleted += 1

    print(f"{model_name}: {added} added, {tagged} tagged, {deleted} deleted")
    return added, tagged, deleted


def do_sync(phase):
    db = sqlite3.connect(PREFS_PATH)
    row = db.execute("select data from profiles where name = ?", (PROFILE_NAME,)).fetchone()
    if row is None:
        raise SystemExit(f"Anki profile not found: {PROFILE_NAME}")
    profile = pickle.loads(row[0])
    hkey = profile.get("syncKey")
    if not hkey:
        raise SystemExit(f"no syncKey in Anki profile {PROFILE_NAME}, log in once from the Anki GUI")
    auth = SyncAuth(hkey=hkey)

    col = Collection(str(COLLECTION_PATH))
    try:
        with redirect_stdout(StringIO()):
            required = col.sync_collection(auth, sync_media=True).required
    finally:
        col.close()

    if required in (0, 1):  # NO_CHANGES, NORMAL_SYNC
        print(f"{phase} complete: {required}")
        return True
    print(f"{phase} requires a full sync ({required}), open Anki once to pick the direction")
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="preview changes without modifying anything")
    parser.add_argument("--no-sync", action="store_true", help="skip the AnkiWeb sync step")
    args = parser.parse_args()

    if not args.dry_run and not args.no_sync:
        if not do_sync("pre-sync"):
            return

    col = Collection(str(COLLECTION_PATH))
    try:
        for nt_dir, (model_name, field_names) in NOTE_TYPES.items():
            mirror_model(col, nt_dir, model_name, field_names, args.dry_run)
        print("dry run, nothing changed" if args.dry_run else "apply complete")
    finally:
        col.close()

    if args.dry_run or args.no_sync:
        return
    do_sync("post-sync")


if __name__ == "__main__":
    main()
