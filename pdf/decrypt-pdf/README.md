# PDF Processing

### Install

```bash
pip3 cache purge
python3 -m venv cache_venv
source cache_venv/bin/activate
pip install -r requirements.txt
```

### Explanation

This Python script removes the password protection from a PDF file and saves the unprotected version. Below is a detailed breakdown of the functionality:
- PyPDF2: The library used to manipulate PDF files in Python.
- `remove_pdf_password(input_pdf_path, output_pdf_path, password)`: This function takes three parameters:
 - `input_pdf_path`: The file path of the password-protected PDF.
 - `output_pdf_path`: The file path where the unprotected PDF will be saved.
 - `password`: The password required to unlock the PDF.
- `reader.is_encrypted`: Checks whether the PDF file is password protected.
- `reader.decrypt(password)`: Decrypts the PDF using the provided password.
- `writer.add_page(reader.pages[page_num])`: Adds each page of the original PDF to a new PDF document.
- `writer.write(output_pdf_file)`: Writes the unprotected PDF to the specified output file.