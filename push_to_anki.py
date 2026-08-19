#!/usr/bin/env python3
"""Push the memory vault into the local Anki collection, then sync to AnkiWeb.

Reads every <note-type>/<deck>/<note-type>_<deck>.txt file in this repo,
adds any notes not already present in the local Anki collection, and syncs
to AnkiWeb so the cards reach every device.

Usage:
  uv run push_to_anki.py          # add missing notes and sync
  uv run push_to_anki.py --dry-run   # preview without changing anything
  uv run push_to_anki.py --no-sync   # add notes locally, skip AnkiWeb sync
"""

import argparse
import html
import pickle
import sqlite3
from pathlib import Path

from anki.collection import Collection
from anki.sync import SyncAuth

REPO = Path(__file__).parent
COLLECTION_PATH = Path.home() / "Library/Application Support/Anki2/Jonah/collection.anki2"
PREFS_PATH = Path.home() / "Library/Application Support/Anki2/prefs21.db"
PROFILE_NAME = "Jonah"

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

# the vault uses these placeholders because quote characters are avoided in its source files
QUOTE_FIXES = {"<single-quote>": "'", "<double-quote>": '"'}


def clean_field(text):
    for placeholder, quote in QUOTE_FIXES.items():
        text = text.replace(placeholder, quote)
    # match what Anki's text importer stores: & < > escaped, quotes left raw
    return html.escape(text, quote=False)


def data_files(note_type_dir):
    return sorted((REPO / note_type_dir).glob("*/*.txt"))


def deck_key_for(data_file, note_type_dir):
    stem = data_file.stem
    prefix = note_type_dir + "_"
    if not stem.startswith(prefix) or stem == prefix:
        raise SystemExit(f"unexpected filename (expected {prefix}<deck>.txt): {data_file}")
    return stem[len(prefix):]


def existing_fields(col, model_name, field_names):
    ids = col.find_notes(f'note:"{model_name}"', order=False)
    existing = set()
    for nid in ids:
        note = col.get_note(nid)
        # stored notes are keyed in the same order the vault files use, by field name
        existing.add(tuple(note[name] for name in field_names))
    return existing


def add_vault_notes(col, dry_run):
    added = 0
    skipped = 0
    for note_type_dir, (model_name, field_names) in NOTE_TYPES.items():
        model = col.models.by_name(model_name)
        if model is None:
            raise SystemExit(f"Anki model not found: {model_name}")
        existing = existing_fields(col, model_name, field_names)
        for data_file in data_files(note_type_dir):
            deck_key = deck_key_for(data_file, note_type_dir)
            deck_name = DECK_MAP.get(deck_key)
            if deck_name is None:
                raise SystemExit(f"no deck mapping for {data_file}: {deck_key}")
            deck = col.decks.by_name(deck_name)
            if deck is None:
                if dry_run:
                    print(f"would create deck: {deck_name}")
                    continue
                deck_id = col.decks.add_normal_deck_with_name(deck_name).id
            else:
                deck_id = deck["id"]
            for line in data_file.read_text().splitlines():
                if not line.strip():
                    continue
                values = line.split("|")
                if len(values) != len(field_names):
                    raise SystemExit(f"expected {len(field_names)} fields, got {len(values)} in {data_file}:\n{line}")
                cleaned = [clean_field(v) for v in values]
                if tuple(cleaned) in existing:
                    skipped += 1
                    continue
                if dry_run:
                    print(f"would add [{deck_name}] {model_name}: {cleaned[0][:60]}")
                    continue
                note = col.new_note(model)
                for name, value in zip(field_names, cleaned):
                    note[name] = value
                col.add_note(note, deck_id)
                existing.add(tuple(cleaned))
                added += 1
    return added, skipped


def do_sync(col):
    db = sqlite3.connect(PREFS_PATH)
    row = db.execute("select data from profiles where name = ?", (PROFILE_NAME,)).fetchone()
    if row is None:
        raise SystemExit(f"Anki profile not found: {PROFILE_NAME}")
    profile = pickle.loads(row[0])
    hkey = profile.get("syncKey")
    if not hkey:
        raise SystemExit(f"no syncKey in Anki profile {PROFILE_NAME}, log in once from the Anki GUI")
    result = col.sync_collection(SyncAuth(hkey=hkey), sync_media=True)
    print(f"sync complete: {result.required}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="preview changes without modifying anything")
    parser.add_argument("--no-sync", action="store_true", help="skip the AnkiWeb sync step")
    args = parser.parse_args()

    col = Collection(str(COLLECTION_PATH))
    try:
        added, skipped = add_vault_notes(col, args.dry_run)
        summary = f"{added} added, {skipped} already present"
        if args.dry_run:
            summary = f"dry run: {summary} (nothing changed)"
        print(summary)
        if not args.dry_run and added:
            print("collection saved")
    finally:
        col.close()

    if args.dry_run:
        return
    if args.no_sync:
        return
    if not args.dry_run:
        col = Collection(str(COLLECTION_PATH))
        try:
            do_sync(col)
        finally:
            col.close()


if __name__ == "__main__":
    main()