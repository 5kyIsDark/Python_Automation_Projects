import datetime 
import os
import csv

target = input("Enter the folder where the files you're interested in exist: ").strip()
csv_filename = "file_report.csv"

with open(csv_filename, "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Filename", "Size (KB)", "Created", "Modified"])  

    for file in os.listdir(target):
        path = os.path.join(target, file)

        if os.path.isdir(path):
            continue

        if os.path.isfile(path): 
            size = os.path.getsize(path) / 1024
            created = datetime.datetime.fromtimestamp(os.path.getctime(path))
            modified = datetime.datetime.fromtimestamp(os.path.getmtime(path))

            print(f"filename --> {file}")
            print(f"size --> {size:.2f} KB")
            print(f"Created --> {created}")
            print(f"Modified --> {modified}")

            writer.writerow([file, f"{size:.2f}", created, modified])

print(f"✅ File details saved to {csv_filename}")


