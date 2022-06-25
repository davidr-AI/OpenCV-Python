from PyPDF2 import PdfFileMerger
import os
pdf = PdfFileMerger()

for file in os.listdir():
    if file.endswith(".pdf"):
        pdf.append(file)

pdf.write("MergedFiles.pdf")
pdf.close()
print("Merge Completed")