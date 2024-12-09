import PyPDF2

def remove_pdf_password(input_pdf_path, output_pdf_path, password):
    with open(input_pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        if reader.is_encrypted:
            reader.decrypt(password)
            writer = PyPDF2.PdfWriter()
            for page_num in range(len(reader.pages)):
                writer.add_page(reader.pages[page_num])
            with open(output_pdf_path, "wb") as output_pdf_file:
                writer.write(output_pdf_file)
            print(f"Password-free PDF saved at: {output_pdf_path}")
        else:
            print("The PDF file is not password protected.")

input_pdf = "input.docs.pdf"
output_pdf = "output.docs.pdf"
password = "secret_password"

remove_pdf_password(input_pdf, output_pdf, password)
