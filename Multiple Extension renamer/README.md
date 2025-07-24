# 🔄 Multiple Extension Renamer

This Python script renames files in a specified folder by converting multiple source file extensions into a single target extension. It's useful for cleaning up inconsistent file formats or normalizing your file structure.

---

## 🚀 Features

- Rename files with multiple specified extensions to a unified extension (e.g., `.text`, `.doc`, `.markdown` → `.txt`)
- Skips subfolders and processes only files
- Displays a success or error message for each file
- Works on Windows, Linux, and macOS

---

## 🛠️ How It Works

1. The user enters the folder path.
2. Then provides a list of extensions to convert **from** (comma-separated, no dot).
3. Finally, provides a single extension to convert **to** (e.g., `.txt`).
4. The script renames all matching files with the new extension.

---

## 📦 Requirements

- Python 3.x  
- No external libraries required (uses only `os`)

---

## 🧪 Example

Suppose your folder has the following files:

```
essay.text  
notes.doc  
summary.markdown  
image.png  
```

If you provide:
- **From Extensions:** `text, doc, markdown`
- **To Extension:** `.txt`

The script renames them to:

```
essay.txt  
notes.txt  
summary.txt  
image.png   ← unchanged
```

---

## 🏁 How to Use

1. Run the script using Python:
   ```bash
   python rename_extensions.py
   ```

2. Provide the required inputs:
   - Folder path containing the files
   - Source extensions (comma-separated, e.g., `text,doc,md`)
   - Target extension (e.g., `.txt`)

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
