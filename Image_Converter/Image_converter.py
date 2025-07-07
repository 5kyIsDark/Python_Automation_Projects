from PIL import Image
import os

target = input("Enter the folder path: ").strip()
choice = input("Convert from (1) JPG to PNG or (2) PNG to JPG? Enter 1 or 2: ").strip()

if choice == "1":
    source_ext = ".jpg"
    target_ext = ".png"
elif choice == "2":
    source_ext = ".png"
    target_ext = ".jpg"
else:
    print("Invalid choice")
    exit()

output_folder = os.path.join(target, "converted")
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(target):
    file_path = os.path.join(target, file)

    if os.path.isdir(file_path):
        continue

    name, ext = os.path.splitext(file)
    if ext.lower() != source_ext:
        continue

    try:
        img = Image.open(file_path)
        if target_ext == ".jpg":
            img = img.convert("RGB")
        new_name = name + target_ext
        new_path = os.path.join(output_folder, new_name)
        img.save(new_path)
        print(f"Converted {file} → {new_name}")
    except Exception as e:
        print(f"Failed to convert {file}: {e}")
