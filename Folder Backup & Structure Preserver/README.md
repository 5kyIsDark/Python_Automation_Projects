# Folder Backup & Structure Preserver 🗂️

This Python script copies all files from a source folder (including all its subfolders) into a destination folder while **preserving the original folder structure**. It's ideal for organized backups or moving entire directory trees without flattening them.

---

## 📌 Features

- Recursively copies all files from source to destination.
- Maintains original subfolder structure.
- Uses `shutil.copy2()` to preserve file metadata (timestamps, etc.).
- Skips existing folders gracefully with `exist_ok=True`.

---

## 🛠️ Requirements

- Python 3.x
- Built-in libraries: `os`, `shutil`

---

## ▶️ How to Use

1. Run the script.
2. Input the full path to the **source folder**.
3. Input the full path to the **destination folder**.

```
Enter the full path of the source folder: C:\Users\John\Documents\Projects
Enter the full path of the destination (backup) folder: D:\Backups\Projects_Backup
```

---

## 📁 Output

- Files are backed up with their full directory paths recreated under the destination.
- For example:
  - `C:\Users\John\Documents\Projects\Python\app.py`
  - → becomes →
  - `D:\Backups\Projects_Backup\Python\app.py`

---

## 🔐 License

This project is licensed under the MIT License.
