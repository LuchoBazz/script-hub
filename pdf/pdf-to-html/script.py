import subprocess
import os

def pdf_to_html(pdf_path, output_html):
    # Check if the PDF file exists
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")

    # Command to convert PDF to HTML
    command = [
        'pdftohtml',  # Command
        '-c',         # Retain image quality
        '-hidden',    # Include hidden text
        '-s',         # Create a single HTML file
        '-noframes',  # Do not use frames
        pdf_path,     # Input PDF path
        output_html   # Output HTML file path
    ]

    try:
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Conversion completed! HTML saved at: {output_html}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during the conversion: {e}")

# Example usage
pdf_file = 'input.pdf'          # Change this to the path of your PDF file
output_file = 'output.html'     # Change this to your desired output path

pdf_to_html(pdf_file, output_file)
