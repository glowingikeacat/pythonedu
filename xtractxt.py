## all deprecations implemented
# March 1, 2023
import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
num_pages = len(pdfReader.pages)
print("Number of pages:", num_pages)


pageObj = pdfReader.pages[0]
#pageObj.extract_text()
page_text = pageObj.extract_text()
print("Page 2 text:", page_text)

pdfFileObj.close()