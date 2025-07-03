import os
import shutil

target = r"C:\Users\KKris\Pictures\Screenshots"
screenshot_folder = os.path.join(target, "screenshot")
os.makedirs(screenshot_folder, exist_ok=True)

prefix = "screenshot"
counter = 1


for file in os.listdir(target):
    file_path = os.path.join(target, file)

    if os.path.isdir(file_path):
        continue

    name, ext = os.path.splitext(file)

    if "screenshot" in name.lower() and ext.lower() == ".png":
        dest_path = os.path.join(screenshot_folder, file)
        shutil.move(file_path, dest_path)
        print(f"✅ Moved {file} to /screenshot")
        

for filename in os.listdir(screenshot_folder):
    file_path = os.path.join(screenshot_folder, filename)

    if os.path.isdir(file_path):
        continue

    _, ext = os.path.splitext(filename)
    new_name = f"{prefix}_{counter}{ext}"
    new_path = os.path.join(screenshot_folder, new_name)

    os.rename(file_path, new_path)
    print(f"🔄 Renamed {filename} → {new_name}")
    counter += 1
