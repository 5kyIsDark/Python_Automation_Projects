import os
import shutil


target_folder = "Downloads"
file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".rar", ".tar"],
    "Code": [".py", ".js", ".html"]
}

for file in os.listdir(target_folder):
    file_path = os.path.join(target_folder, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    _, ext = os.path.splitext(file)

    moved = False
    for folder, extensions in file_types.items():
        if ext.lower() in extensions:
            dest_folder = os.path.join(target_folder, folder)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, file))
            print(f"Moved {file} to {folder}/")
            moved = True
            break

    if not moved:
        print(f"Skipped {file} (unknown type)")
