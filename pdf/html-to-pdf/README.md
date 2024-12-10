# HTML to PDF

```bash
pip3 cache purge
python3 -m venv cache_venv
source cache_venv/bin/activate
pip install -r requirements.txt
```

## Generating PDF from HTML

To generate a PDF file from an HTML document, the `WeasyPrint` library can be utilized. First, ensure that the library is installed via pip:

```bash
pip install WeasyPrint
```

### Explanation

After converting the PDF to HTML, the `WeasyPrint` library can be used to generate a PDF file from an HTML document. This library provides a straightforward interface for rendering HTML to PDF, ensuring that the output maintains the original document's structure and styling.
