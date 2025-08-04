# 📄 PDF Merger

A Python script that merges all PDF files in a folder into a single combined PDF.

## Features

- Merges multiple .pdf files into one
- Prompts for custom output file name
- Automatically sorts files before merging

## How to Use

1. Run the script:

   python pdf_merger.py

2. Enter the full folder path containing your PDF files
3. Enter the desired name for the merged PDF
4. The combined file will be saved in the same folder

## Example

Input:
folder/
├── page1.pdf
├── page2.pdf

Output:
folder/
└── final_output.pdf

## Requirements

- Python 3.x
- Install PyPDF2:

  pip install PyPDF2


## Alternate Of The Code (PDF_Folder_Merger)

- It Merges all the PDF's in a folder (including the one's hidden deep within subfolders)

