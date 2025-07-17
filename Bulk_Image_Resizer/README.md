# Image Resizer (with Aspect Ratio Preservation)

This Python script resizes all image files in a specified folder to a fixed width (default: **800 pixels**) while maintaining their original aspect ratio. It supports popular image formats like `.jpg`, `.jpeg`, `.png`, `.bmp`, and `.gif`.

## 🛠 Features

- Automatically resizes all image files in a folder
- Maintains the original aspect ratio
- Supports multiple image file types
- Saves resized images to a `Resized_Images` folder
- Skips non-image files and subfolders
- Provides error handling and success messages

## 📦 Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) library

You can install Pillow with:

```bash
pip install pillow
```

## 🚀 How to Use

1. Run the script.
2. Enter the full file path to the folder containing your images.
3. The script will:
   - Resize each image to 800 pixels wide
   - Adjust the height automatically to preserve the aspect ratio
   - Save all resized images into a folder named `Resized_Images` inside the current working directory.

## 📝 Notes

- Files that are not valid image types will be ignored.
- Images that fail to open or resize will be reported with an error message.
- You can modify the `new_width` variable in the script to set a different target width.

## 📄 License

MIT License

---

🔧 Made for automation and beginner Python practice.
