import os
from PyPDF2 import PdfWriter

merge = PdfWriter()
path = r'D:\100_Days_of_Code\00_Exercises\04_Merge_PDF\pdfs'
files = os.listdir(path)
for pdf in files:
    if pdf.endswith(".pdf"):
        merge.append(os.path.join(path, pdf))

new_pdf = merge.write("Merged-PDF.pdf")
merge.close()

os.rename("Merged-PDF.pdf",f"{path}/Merged-PDF-2025.pdf")