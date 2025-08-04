import os
from PyPDF2 import PdfMerger

folder = input("please Enter The filepath Containing the PDf files: ").strip()

output_name = input("Enter The name for the merged PDF (without .pdf): ").strip()+".pdf"

pdf_files = [f for f in os.listdir(folder) if f.lower().endswith(".pdf") ]
pdf_files.sort()

merger = PdfMerger()

for file in pdf_files:
    file_path = os.path.join(folder,file)
    merger.append(file_path)
    print(f"added {file}")

output_path = os.path.join(folder, output_name)
merger.write(output_path)
merger.close()

print(f"Merged Pdg saved as {output_path}")

