import pyttsx3
import PyPDF2
book = open('Head First JavaScript Programming A Brain-Friendly Guide ( PDFDrive ).pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
# how many pages the book has
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
# starts from page number 7...
for num in range(7, pages):
    page = pdfReader.getPage(num)
    # extracting the text
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()