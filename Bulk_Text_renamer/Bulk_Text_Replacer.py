import os
import shutil
import re

target_file = input("Please Enter The Full Path To The Folder In which you have your Files: ")

target_word = input("Input The word or Phrase You Would Like to Replace: ")

replaced = input("Input The Word or phrase to replace the choosen word/Phrase : ")

ext_filter = "txt"
for file in os.listdir(target_file):
    file_path = os.path.join(target_file, file)


    if os.path.isdir(file_path):
        continue

    name, ext = os.path.splitext(file)

    if ext_filter and ext != f".{ext_filter}":
        continue


    shutil.copy(file_path, file_path + ".bak")

    try:
        with open(file_path, "r", encoding="utf-8") as fila:
            content = fila.read()
        count = content.count(target_word)
        updated_content = re.sub(target_word, replaced, content, flags=re.IGNORECASE)

        with open(file_path, "w", encoding="utf-8") as fila:
            fila.write(updated_content)

        print(f" {count} replacements made in {file}")

    except Exception as e:
        print(f" could not make changes to {file}: {e} ")

