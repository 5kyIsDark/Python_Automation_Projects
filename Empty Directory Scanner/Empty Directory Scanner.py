import os

target = input("Enter the root folder path to scan for empty folders: ").strip()

empty_folders = []


for foldername, subfolders, filenames in os.walk(target, topdown=False):
    if not os.listdir(foldername): 
        try:
            os.rmdir(foldername)
            empty_folders.append(foldername)
            print(f"🗑️ Removed empty folder: {foldername}")
        except Exception as e:
            print(f"❌ Could not remove {foldername}: {e}")

if empty_folders:
    print("\n✅ Empty folders removed successfully.")
else:
    print("📁 No empty folders found.")
