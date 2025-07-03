# 🗂️ File Organizer (by Extension)

A Python script that organizes files in a folder into subfolders based on file type (e.g., images, videos, documents).

## Features

- Automatically sorts files into folders like `Images/`, `Videos/`, `Documents/`, etc.
- Recognizes common file extensions
- Creates folders if they don’t exist
- Cleans up cluttered folders like Downloads/Desktop

## How to Use

1. Run the script:

   python file_organizer.py

2. When prompted, enter the full path of the folder you want to organize (e.g., C:\Users\YourName\Downloads)

3. Files will be moved into subfolders based on their extensions.

## Example

Before:
Downloads/
├── photo.jpg
├── resume.pdf
├── script.py

After:
Downloads/
├── Images/photo.jpg
├── Documents/resume.pdf
├── Code/script.py

## Requirements

- Python 3.x
- Built-in modules: os, shutil
