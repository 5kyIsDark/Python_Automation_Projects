# 🧹 Empty Directory Scanner

This is a simple Python automation script that scans a given directory and its subdirectories to identify and delete **empty folders**. It's useful for cleaning up clutter in large directory trees.

## 📦 Features

- Recursively scans all subfolders.
- Deletes only empty folders.
- Bottom-up scanning ensures parent folders are also removed if they become empty after child deletions.
- Provides informative output for every action taken.

## 🛠️ How It Works

The script uses Python’s `os` module and walks through the folder tree **bottom-up** (using `os.walk(topdown=False)`). It checks each folder for contents using `os.listdir()`, and if found empty, removes it using `os.rmdir()`.

## ▶️ How to Use

1. Run the script.
2. When prompted, enter the full path of the folder you want to scan.
3. The script will remove all empty folders inside it (including nested ones).
4. You’ll see a list of all deleted folders or a message if no empty folders were found.

## 💡 Example

```
Enter the root folder path to scan for empty folders: C:\Users\Krishik\Documents\Projects
🗑️ Removed empty folder: C:\Users\Krishik\Documents\Projects\Old
🗑️ Removed empty folder: C:\Users\Krishik\Documents\Projects\Drafts\Temp
✅ Empty folders removed successfully.
```

## 📋 Requirements

- Python 3.x


