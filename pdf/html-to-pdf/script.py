from weasyprint import HTML

# Path to the HTML file
input_file = 'output.html'

# Generate the PDF from the HTML file
HTML(input_file).write_pdf('output.pdf')

print("PDF generated successfully.")
