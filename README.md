# Memory 🧠

Welcome to **Memory**, a simple Git repository for organizing and managing data for my [Anki](https://github.com/ankitects/anki) decks. This repo allows me to use IDE tools to easily add, edit, and version-control notes before importing them into Anki for long-term retention.

## 📚 Introduction

This repository stores notes in a structured format that's easy to read, edit, and import into Anki. The primary goal is to leverage version control for my learning materials, making it simple to track changes and collaborate if needed.

## ✨ Features

- **Easy Editing**: Use your favorite IDE to add or modify notes.
- **Anki-Compatible Format**: Notes are stored in pipe-separated format ready for Anki import.
- **Version Control**: Track changes to your notes over time with Git.
- **Organized Structure**: Notes grouped by deck/topic for better management.

## 📝 Usage

### Repository Structure
The repository contains note types organized as:
- **`<note-type>/`**: Top-level directories for different types of flashcards
  - `<deck>/notes.txt`: Pipe-separated note data for a specific deck

**Example structure:**
```
quotes/
├── us-presidents/
│   └── notes.txt    # Presidential quotes
└── world-leaders/
    └── notes.txt    # Other leader quotes

us-presidents-info/
└── us-presidents/
    └── notes.txt    # Basic presidential facts
```

### File Format
Notes are stored in `.txt` files with pipe (`|`) separated values. The format varies by note type:

**Simple two-column format** (e.g., quotes):
```
Author|Quote
Thomas Jefferson|The tree of liberty must be refreshed from time to time with the blood of patriots and tyrants.
```

**Multi-column format** (e.g., detailed info):
```
Number|Name|Terms|Party|Summary
1|George Washington|1789 - 1797|Unaffiliated|Led the Continental Army; first president; set the two-term precedent
```

### Adding New Notes
1. Navigate to the appropriate note type directory.
2. Open the `notes.txt` file in the relevant deck subdirectory.
3. Add new lines following the established format for that note type:
   - Use pipe (`|`) as field separator
   - Maintain consistent column structure within each note type
   - No headers in the file itself
4. Commit changes: `git add . && git commit -m "Add new notes"`

### Creating New Note Types
1. Create a new top-level directory with descriptive name (e.g., `world-capitals/`).
2. Inside, create a deck subdirectory (e.g., `geography/`).
3. Create `notes.txt` with your desired pipe-separated format.
4. Consider adding documentation files:
   - `fields.md`: Description of each field/column
   - `cards.md`: Anki card templates
   - `guidelines.md`: Style guide for adding notes

### Importing to Anki
1. Copy the `notes.txt` file you want to import
2. Convert pipes to tabs if needed for Anki compatibility
3. Import via Anki's File > Import feature
4. Map fields appropriately during import

## 🤝 Contributing

Feel free to fork and submit pull requests! When adding new content:
- Follow existing format conventions for each note type
- Use consistent pipe separation
- Maintain clear, factual content
- Update this README if adding new note types

Happy learning! 🚀
