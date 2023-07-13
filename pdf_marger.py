# pip install PyPDF2

import PyPDF2

pdfiles = ["1.pdf","2.pdf","3.pdf"]

marger = PyPDF2.PdfMerger()

for filename in pdfiles:
    pdfFile=open(filename,'rb')
    pdfreader=PyPDF2.PdfReader(pdfFile)
    marger.append(pdfreader)

marger.write("merged_2_pages.pdf")
marger.close()
