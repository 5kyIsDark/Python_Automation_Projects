# 🔤 Bulk File Renamer

A Python script to rename all files in a folder using a prefix and optional extension filter.

## Features

- Renames files using a prefix + counter (e.g., image_1.png)
- Optional extension filter (e.g., only .jpg files)
- Skips folders automatically

## How to Use

1. Run the script:

   python file_renamer.py

2. Enter:
   - Folder path
   - Prefix (e.g., file, image)
   - Optional extension filter (e.g., jpg)

3. Files will be renamed as prefix_1.ext, prefix_2.ext, etc.

## Example

Before:
photos/
├── a.jpg
├── b.jpg

After:
photos/
├── vacation_1.jpg
├── vacation_2.jpg

## Requirements

- Python 3.x
- Built-in module: os
