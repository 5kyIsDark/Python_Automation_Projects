# ✏️ Bulk Text Replacer (TXT Files)

This Python script automates the process of finding and replacing a word or phrase in all `.txt` files within a selected folder. It performs case-insensitive replacement and creates a backup of each file before modifying it.

## ✅ Features

- Replace any word or phrase across all `.txt` files
- Case-insensitive matching using regular expressions
- Automatically skips folders and non-text files
- Creates a `.bak` backup for every edited file
- Displays how many replacements were made per file

## 💻 How to Use

1. Run the script

2. Enter the following when prompted:
   - Folder path containing the `.txt` files
   - The word/phrase to search for
   - The replacement word/phrase

3. Done! The script will:
   - Replace all matching text (case-insensitive)
   - Save changes back to each file
   - Create a `.bak` backup of the original

## 🧪 Example

**Before (`sample.txt`):**

Python is awesome.  
PYTHON makes automation easy.

**After replacement:**

JavaScript is awesome.  
JavaScript makes automation easy.

**Backup file created:**

sample.txt.bak

## 📦 Requirements

- Python 3.x
- Uses built-in libraries:
  - os
  - shutil
  - re
