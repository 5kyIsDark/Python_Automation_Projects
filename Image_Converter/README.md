# 🖼️ Image Format Converter (JPG ↔ PNG)

This Python automation tool allows you to convert all `.jpg` images in a folder to `.png`, or `.png` images to `.jpg`. The converted files are saved in a `converted/` subfolder inside the original directory.

---

## ✅ Features

- Convert from **JPG to PNG** or **PNG to JPG**
- Batch process all images in a selected folder
- Creates a `converted/` output folder automatically
- Preserves original images
- Handles transparency issues when converting PNG to JPG

---

## 💻 How to Use

1. Make sure you have **Python 3.x** installed  
2. Install the required library:  
   `pip install pillow`  
3. Run the script:  
   `python image_converter.py`  
4. When prompted:
   - Enter the **folder path** containing your images
   - Choose conversion mode:
     - `1` → JPG to PNG
     - `2` → PNG to JPG

---


---

## 🛠 Requirements

- Python 3.x
- Pillow (`pip install pillow`)

---

## ⚠️ Notes

- The script skips subfolders and non-image files
- When converting PNG → JPG, images are flattened to RGB to avoid alpha channel issues

---

## 📦 License

This project is open-source and free to use.
