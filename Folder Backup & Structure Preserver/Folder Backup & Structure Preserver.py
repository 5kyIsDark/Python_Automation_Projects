import os
import shutil


source_folder = input("Enter the full path of the source folder: ").strip()
destination_folder = input("Enter the full path of the destination (backup) folder: ").strip()


for foldername, subfolders, filenames in os.walk(source_folder):
    for filename in filenames:
        
        source_path = os.path.join(foldername, filename)


        relative_path = os.path.relpath(source_path, start=source_folder)


        dest_path = os.path.join(destination_folder, relative_path)


        os.makedirs(os.path.dirname(dest_path), exist_ok=True)


        shutil.copy2(source_path, dest_path)


        print(f"✅ Copied: {source_path} → {dest_path}")


print("\n🎉 All files copied successfully with folder structure preserved.")
