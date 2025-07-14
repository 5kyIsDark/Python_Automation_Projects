# 📄 PDF Page Splitter (Python Automation)

This simple Python script takes a multi-page PDF and splits each page into its own separate PDF file.

---

## ✅ Features

- Splits a single PDF into multiple one-page PDFs
- Automatically names files like `page_1.pdf`, `page_2.pdf`, etc.
- Saves output to a folder called `Split_Pages`
- Works on any PDF with two or more pages

---

## 🧰 Requirements

- Python 3.x
- `PyPDF2` library

### 🔧 Install the library:
```bash
pip install PyPDF2
```

---

## 🚀 How to Use

1. Run the script:
   ```bash
   python pdf_splitter.py
   ```

2. Enter the full file path of the PDF when prompted:
   ```
   Enter The File Path Of The PDF File:
   ```

3. After running, check the `Split_Pages/` folder — you'll find:
   ```
   Split_Pages/
   ├── page_1.pdf
   ├── page_2.pdf
   ├── ...
   ```

---

## 📁 Project Structure

```
pdf_splitter.py
Split_Pages/
    page_1.pdf
    page_2.pdf
    ...
```

---

## 🧠 Use Cases

- Breaking down scanned PDFs into separate pages
- Extracting individual invoices or forms
- Automating document organization

---

## 🛡️ License

This project is free and open-source under the MIT License.
