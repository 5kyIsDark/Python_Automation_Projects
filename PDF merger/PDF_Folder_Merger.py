import os
from PyPDF2 import PdfMerger


target = input("Enter the folder with all the PDFs you would like to merge: ").strip()
output_name = input("Enter the name of the PDF after merging: ").strip() + ".pdf"


merger = PdfMerger()


for foldername, subfoldernames, filenames in os.walk(target):
    for filename in sorted(filenames):  
        if filename.lower().endswith('.pdf'):
            path = os.path.join(foldername, filename)
            merger.append(path)
            print(f"File added: {path}")


output_path = os.path.join(target, output_name)
merger.write(output_path)
merger.close()
print(f"Merged PDF saved as: {output_path}")
