import PyPDF2

with open('document.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    print(page.extract_text())
