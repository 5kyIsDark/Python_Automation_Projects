import os


target_folder = input("Enter the folder path containing the files: ").strip()


from_exts = input("Enter the extensions to convert from (comma-separated, e.g., text,doc,markdown): ").strip().lower().split(",")
from_exts = [f".{ext.strip()}" for ext in from_exts]


to_ext = input("Enter the extension to convert to (e.g., .txt): ").strip().lower()
if not to_ext.startswith("."):
    to_ext = "." + to_ext


for file in os.listdir(target_folder):
    file_path = os.path.join(target_folder, file)

    if os.path.isdir(file_path):
        continue

    name, ext = os.path.splitext(file)
    if ext.lower() in from_exts:
        new_filename = name + to_ext
        new_path = os.path.join(target_folder, new_filename)

        try:
            os.rename(file_path, new_path)
            print(f"✅ Renamed: {file} → {new_filename}")
        except Exception as e:
            print(f"❌ Failed to rename {file}: {e}")

print("\n🎉 Renaming completed.")
