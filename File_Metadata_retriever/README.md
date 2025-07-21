# 📁 File Metadata Reporter

This Python script scans a target folder, collects metadata for all files, and writes the information to a CSV report. The details include:

- File name
- File size (in KB)
- Creation date
- Last modification date

## 🧰 Features

- Supports all file types
- Outputs metadata into a clean CSV file
- Shows live file details in the console
- Supports UTF-8 encoding

## 📦 Requirements

- Python 3.x
- No external libraries required

## 🚀 How to Use

1. Run the script.
2. Enter the full path to the folder you want to scan.
3. The script will:
   - Print metadata for each file in the terminal
   - Save all metadata in a `file_report.csv` file in the current directory

## 📄 Output Format (CSV Columns)

| Filename | Size (KB) | Created | Modified |
|----------|-----------|---------|----------|

## 📌 Notes

- Subfolders are not scanned by default. To include them, you can use `os.walk()` instead of `os.listdir()`.
- You can customize filters for file types or size if needed.

## 🔖 License

MIT License

