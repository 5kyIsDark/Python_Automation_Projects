# 🧹 Temporary File Cleaner (Python)

This Python script scans a folder (and all its subfolders) for common temporary file types and deletes them. It also logs all actions in a file called `file_operations.log`.

---

## 🚀 Features

- Recursively scans a target directory for temporary files
- Deletes files with extensions like `.tmp`, `.log`, `.bak`, etc.
- Logs every deleted file with timestamps
- Handles deletion errors gracefully

---

## 🛠️ Temporary File Types Targeted

The script deletes files with the following extensions:

- `.tmp`
- `.log`
- `.bak`
- `.old`
- `.chk`
- `.dmp`
- `.temp`
- `.cache`

You can customize the extensions in the `temp_ext` set in the code.

---

## 📦 How to Use

1. **Install Python (if not already installed)**  
   This script requires Python 3.6+

2. **Run the Script**

```bash
python temp_file_cleaner.py
```

3. **Follow the prompt**  
   Enter the path to the folder you want to clean when prompted.

---

## 📄 Log File

All actions are logged in:

```
file_operations.log
```

This log includes:
- Which files were deleted
- Any errors encountered

---

## 🔐 Disclaimer

> This script **permanently deletes files**. Make sure you understand what file types you’re targeting before running it on important folders.

---

## 📃 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
