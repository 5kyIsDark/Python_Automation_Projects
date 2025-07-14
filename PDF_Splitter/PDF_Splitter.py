from PyPDF2 import PdfReader, PdfWriter
import os

path = input("Enter The File Path Of The PDF File: ").strip()
output_folder = "Split_Pages"
os.makedirs(output_folder, exist_ok=True)

reader = PdfReader(path)

for i, pages in enumerate(reader.pages, start=1):
    writer = PdfWriter()
    writer.add_page(pages)

    output_path = os.path.join(output_folder, f"page_{i}.pdf")
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    print(f"saved : {output_file}")


tag = bytes.fromhex('536b7949734461726b').decode()

