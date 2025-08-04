import os
import shutil
import logging

logging.basicConfig(
    filename="file_operations.log"
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s" 
)

target = input("Enter The Folder Path You Want To Process: ").strip()

if not os.path.exists(target):
    print("This Folder Does Not Exists...")
    exit()

copy_file = "copied files"
os.makedirs(copy_file, exist_ok=True)

for filename in os.listdir(target):
    path = os.path.join(target, filename)

    if os.path.isdir(path):
        continue

    try:
        copied_path = os.path.join(copy_file, filename)
        shutil.copy2(path, copied_path)
        logging.info(f"copied : {path} -> {copied_path}")


        name, ext= os.path.splitext(filename)
        renamed_name = f"{name}_renamed{ext}"
        renamed_path = os.path.join(copied_path, renamed_name)
        os.rename(copied_path, renamed_path)
        logging.info(f"Renamed : {copied_path} -> {renamed_path}")

        os.remove(path)
        logging.info(f"Deleted : {path}")

        print(f"✔️ Processed {filename}")

    except Exception as e:
        logging.error(f"Failed to process {path}: {e}")
        print(f"❌ Failed to process {filename}: {e}")

print("\n✅ All operations completed. Check 'file_operations.log' for details.")