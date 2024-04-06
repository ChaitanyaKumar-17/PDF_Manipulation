from pypdf import PdfWriter
pdfs=[]                                #all the pdf names(with .pdf) in the order of merging
merger=PdfWriter()

#loop through all the pdfs and merge it
for pdf in pdfs:
    merger.append(pdf)

#add the pdf to a new a pdf
merger.write("merged.pdf")
merger.close()
print("Success!!!")



'''
alternatively:-
merger.append("doc1.pdf)
merger.append("doc2.pdf", pages=(start_page,end_page,step_value))
'''