# 🗃️ File Organizer & Logger

This is a simple Python automation script that **copies**, **renames**, and **deletes** files in a specified folder while keeping a detailed log of every operation.

---

## ✅ Features

- ✅ Copies all files from a target folder into a new folder (`copied_files`)
- ✅ Renames the copied files by appending `_renamed` to their names
- ✅ Deletes the original files from the target folder
- ✅ Logs all actions (copy, rename, delete) into `file_operations.log`
- ✅ Skips directories automatically

---

## 📦 Requirements

- Python 3.x
- No external libraries required (uses built-in `os`, `shutil`, and `logging`)

---

## 🚀 How to Use

1. Make sure you have Python 3 installed.
2. Place the script in any directory.
3. Run the script using:

```bash
python file_organizer.py
```

4. When prompted, enter the full path of the folder whose files you want to process.

---

## 📁 Output

- All copied and renamed files are stored in a new folder called `copied_files`
- A log file named `file_operations.log` is created in the same directory to track:
  - Files copied
  - Files renamed
  - Files deleted
  - Any errors encountered

---

## 🛑 Notes

- Subfolders are skipped (only files in the top-level folder are processed).
- If a file with the same renamed name already exists in the output folder, it will be **overwritten**.
- You can open `file_operations.log` in any text editor to view operation history.

---

## 🔒 License

This project is licensed under the **MIT License** — free for personal or commercial use.

---

## ✨ Author

Built by an aspiring Python automation and cybersecurity enthusiast 💻🔐
