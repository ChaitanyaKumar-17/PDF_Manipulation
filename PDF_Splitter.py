from pypdf import PdfReader, PdfWriter

input_pdf_path = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\git-github-reference.pdf"     # Replace 'your_file.pdf' with the path to your PDF file

pdf_reader = PdfReader(input_pdf_path)

total_pages = len(pdf_reader.pages)

pd1=list(range(0,3))
pd2=list(range(3,7))

#and so onnnnn

pdf1_writer = PdfWriter()
pdf2_writer = PdfWriter()

#and so onnnnn

# Loop through each page and save it on a separate PDFwriter
for page in range(total_pages):
    if page in pd1:
        pdf1_writer.add_page(pdf_reader.pages[page])
    elif page in pd2:
        pdf2_writer.add_page(pdf_reader.pages[page])
    #and so onnnnnn
    
# Write the pages to a new PDF
with open("pdf1.pdf", 'wb') as p1:
        pdf1_writer.write(p1)

with open("pdf2.pdf", 'wb') as p2:
        pdf2_writer.write(p2)

print("Success!!!!!")
