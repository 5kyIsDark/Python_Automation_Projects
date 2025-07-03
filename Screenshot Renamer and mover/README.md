# 🖼️ Screenshot Mover & Renamer

A Python script that moves .png screenshots into a subfolder and renames them using a prefix.

## Features

- Moves all .png files to a screenshots/ folder
- Renames them as prefix_1.png, prefix_2.png, etc.
- Automatically creates the destination folder if needed

## How to Use

1. Run the script:

   python screenshot_mover.py

2. Enter:
   - Folder path where the screenshots are
   - A prefix (e.g., screenshot)

3. Screenshots will be moved and renamed inside screenshots/.

## Example

Before:
Pictures/
├── 2024-06-01.png
├── 2024-06-02.png

After:
Pictures/screenshots/
├── screenshot_1.png
├── screenshot_2.png

## Requirements

- Python 3.x
- Built-in modules: os, shutil
