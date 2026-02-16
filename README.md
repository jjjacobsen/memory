# Memory 🧠

Welcome to **Memory**, a simple Git repository for organizing and managing data for my [Anki](https://github.com/ankitects/anki) decks. This repo allows me to use IDE tools to easily add, edit, and version-control notes before importing them into Anki for long-term retention.

## 📚 Introduction

This repository stores notes in a structured format that's easy to read, edit, and import into Anki. The primary goal is to leverage version control for my learning materials, making it simple to track changes and collaborate if needed.

## 📝 Usage

### Repository Structure
The repository contains note types organized as:
- **`<note-type>/`**: Top-level directories for different types of flashcards
  - `fields.md`: Documentation describing each field/column in the notes
  - `cards.md`: Anki card templates and formatting instructions
  - `<deck>/notes.txt`: Pipe-separated note data for a specific deck

**Example structure:**
```
quotes/
├── fields.md        # Field descriptions (Author, Quote, etc.)
├── cards.md         # Card templates for quote formatting
└── us-presidents/
    └── notes.txt    # Presidential quotes data
```

### File Format
Notes are stored in `.txt` files with pipe (`|`) separated values. The format varies by note type and is documented in each `fields.md` file.

**Simple two-column format** (e.g., quotes):
```
Author|Quote
Thomas Jefferson|The tree of liberty must be refreshed from time to time with the blood of patriots and tyrants.
```

**Multi-column format** (e.g., detailed info):
```
Number|Name|Term|Party|State
1|George Washington|1789 - 1797|Unaffiliated|Virginia
```

### Adding New Notes
1. Navigate to the appropriate note type directory.
2. Review the `fields.md` file to understand the field structure.
3. Open the `notes.txt` file in the relevant deck subdirectory.
4. Add new lines following the established format:
   - Use pipe (`|`) as field separator
   - Maintain consistent column structure as defined in `fields.md`
   - No headers in the file itself

### Creating New Note Types
1. Create a new top-level directory with descriptive name (e.g., `world-capitals/`).
2. Create documentation files:
   - `fields.md`: Description of each field/column
   - `cards.md`: Anki card templates and formatting instructions
3. Create a deck subdirectory (e.g., `geography/`).
4. Create `notes.txt` with your desired pipe-separated format.

### Importing to Anki
1. Review the `cards.md` file for the note type to understand card templates.
2. Copy the `notes.txt` file you want to import.
3. Import via Anki's File > Import feature.
4. Map fields appropriately during import using the `fields.md` documentation.
    - Make sure to disable `Allow HTML in fields`
    - Avoid using `'` and `"`. The import gets weird
5. Apply card templates as described in `cards.md`.
