import os 
import hashlib


def get_hash_file(file_path):
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()


file_hashes = {}
duplicates = []



target = input("Enter The Folder You Would Like To Scan: ").strip()

for foldername, subfolder, filenames in os.walk(target):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)

        try:
            file_hash = get_hash_file(file_path)
        except Exception as e:
            print(f"Could Not Read File {file_path}: {e}")
            continue

        if file_hash in file_hashes:
            duplicates.append((file_path, file_hashes[file_hash]))
        else:
            file_hashes[file_hash] = file_path


if duplicates:
    print("\n🧹 Duplicate Files Found:")
    for dup, original in duplicates:
        print(f"❌ {dup} (same as {original})")
else:
    print("✅ No duplicates found.")
