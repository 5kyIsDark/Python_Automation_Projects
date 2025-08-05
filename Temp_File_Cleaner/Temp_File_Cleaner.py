import os
import logging

# Corrected logging setup (you had syntax errors here)
logging.basicConfig(
    filename="file_operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


temp_ext = {".tmp", ".log", ".bak", ".old", ".chk", ".dmp", ".temp", ".cache"}


target = input("Enter the folder you would like to scan for temp files: ").strip()

if not os.path.exists(target):
    print("❌ This folder does not exist...")
    exit()

for foldername, subfolders, filenames in os.walk(target):
    for file in filenames:
        name, ext = os.path.splitext(file)

        if ext.lower() not in temp_ext:
            continue

        file_path = os.path.join(foldername, file)

        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                logging.info(f"Deleted: {file_path}")
                print(f"🗑️ Deleted: {file_path}")
            except Exception as e:
                logging.error(f"Failed to delete {file_path}: {e}")
                print(f"❌ Failed to delete {file_path}: {e}")

print("\n✅ All operations completed. Check 'file_operations.log' for details.")
