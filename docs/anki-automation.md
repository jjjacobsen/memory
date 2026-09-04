# Anki automation

How the memory vault gets into Anki without ever opening the Anki app

## Pipeline

```
vault .txt files --(push_to_anki.py)--> local collection --(sync)--> AnkiWeb
```

1. `push_to_anki.py` opens the local Anki collection directly with the `anki`
   Python library (same version as the installed Anki app, currently 26.8.1)
2. It reads every `<note-type>/<deck>/<note-type>_<deck>.txt` file
3. It mirrors the vault into the collection: adds new notes, replaces edited
   ones, and deletes cards whose lines are gone from the vault
4. It syncs the collection to AnkiWeb using the `syncKey` the Anki app already
   stores in `prefs21.db`, so the cards reach every device

The vault is the source of truth. Anything in Anki that is not in the vault
and is managed by the script gets removed on the next push.

## Commands

- `mise run anki-preview` dry run, shows what would be added, tagged, and
  deleted without touching anything
- `mise run anki-push` mirror the vault locally then sync to AnkiWeb
- `uv run push_to_anki.py --dry-run` same as anki-preview
- `uv run push_to_anki.py --no-sync` mirror locally without syncing

## Mirror semantics

Every note the script owns carries the tag `memory-vault`. On each run, for
each managed note type:

- a vault line with no matching note is added (new card)
- a managed note whose line is gone is deleted
- editing a line counts as add new plus delete old, so a replaced card starts
  a fresh review schedule

Only notes tagged `memory-vault` are ever deleted. A note you add directly in
Anki is safe unless it exactly matches a vault line, in which case the script
adopts it (tags it) and keeps it in sync with the vault from then on.

Always run `mise run anki-preview` first to see what would be deleted.

## Configuration

Hardcoded at the top of `push_to_anki.py` for the Omarchy/Linux installation:

- `ANKI_DATA` is `~/.local/share/Anki2`
- `COLLECTION_PATH` is the `User 1` profile's `collection.anki2`
- `PREFS_PATH` and `PROFILE_NAME` locate the `User 1` AnkiWeb `syncKey`
- `NOTE_TYPES` maps each note-type directory to its Anki model name and the
  field order used in the vault files
- `DECK_MAP` maps each deck directory name to its Anki deck name

New note types or decks need a new entry in those two dicts.

## Data conventions

- One note per line, pipe separated, no header row
- Field names and order defined in each note type's `fields.md`
- Real quote characters are fine, the script HTML-escapes field text the same
  way Anki's importer does (`& < >` escaped, quotes left raw)
- `;` and `;;` inside a field are line-break delimiters, converted to `<br>`
  by JavaScript in the card template (prayers, linux-sys-admin)
- Matching is by exact content per model, so whitespace and quoting must stay
  consistent between the vault and Anki. Fields are stripped and escaped
  before matching

## Models and templates

The Anki models and their card templates live in the Anki collection. Each
note type's `cards.md` mirrors the same Front, Back and Styling code so the
repo documents what runs in Anki. When templates change, update both.

## Notes

- The `anki` pip package version must match the installed Anki app version so
  the collection schema stays compatible (no upgrade, no downgrade)
- Close the Anki desktop app before running a preview or push because both
  programs open the same collection database
- The sync login is reused from the desktop app, no password is needed and
  nothing is stored in this repo
- First sync after a long gap may ask AnkiWeb to select full upload or
  download, same as the app would
- AnkiWeb requires the account email to be confirmed before syncing. If the
  sync reports that the email needs (re)confirmation, log in at ankiweb.net
  as the stored account and confirm it, then sync again
