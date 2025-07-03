import os

folder = input("📂 Enter the folder path: ").strip()
prefix = input("🔤 Enter the prefix for new filenames: ").strip()
ext_filter = input("🧪 Enter file extension to filter by (or leave blank for all): ").strip().lower()

if not os.path.exists(folder):
    print("❌ Folder does not exist.")
    exit()

counter = 1
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    if os.path.isdir(file_path):
        continue

    name, ext = os.path.splitext(filename)

    if ext_filter and ext.lower() != f".{ext_filter}":
        continue

    new_name = f"{prefix}_{counter}{ext}"
    new_path = os.path.join(folder, new_name)

    os.rename(file_path, new_path)
    print(f"✅ Renamed {filename} → {new_name}")
    counter += 1

print(f"\n🎉 Done! Renamed {counter - 1} file(s).")
