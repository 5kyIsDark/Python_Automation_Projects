# 🔍 Duplicate File Finder (Python Automation)

This Python script scans a folder (including all subfolders) and detects duplicate files based on their content using file hashing.

---

## 📌 Features

- Recursively scans folders and subfolders
- Compares files using their **MD5 hash**
- Reports duplicate file pairs clearly
- Handles unreadable files gracefully

---

## 💻 How to Use

1. **Install Python** (version 3.6 or later)

2. **Run the script**:
   ```bash
   python duplicate_finder.py
   ```

3. **Enter the folder path** when prompted:
   ```
   Enter The Folder You Would Like To Scan:
   ```

4. ✅ Output example:
   ```
   🧹 Duplicate Files Found:
   ❌ D:\Photos\copy1.jpg (same as D:\Photos\original.jpg)
   ❌ D:\Docs\backup.txt (same as D:\Docs\main.txt)
   ```

---

## ⚙️ How It Works

- Uses `os.walk()` to loop through all files
- Reads each file in binary mode
- Computes a **MD5 hash** using `hashlib`
- If two files share the same hash → marked as duplicates

---

## 📁 Project Structure

```
duplicate_finder.py
```

---

## 🧠 Tip

To delete or move duplicates, you can extend this script easily!

---

## 📦 Dependencies

- Python 3.x (no external packages required)

---

## 🛡️ License

This project is free and open-source under the MIT license.
