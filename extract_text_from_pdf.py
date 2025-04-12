import PyPDF2
'''
PyPDF2 is a Python library used for working with PDF files. It allows you to perform a variety of tasks, such as:
-> Extracting Text
-> Merging PDFs
-> Splitting PDFs
-> Rotating Pages
-> Adding Watermarks
-> Encrypting and Decrypting PDFs
'''

# Create a pdf file object
pdfFileObj = open("bayesian_learning.pdf", 'rb') #rb- read binary mode

# Create a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Display total number of pages in pdf file
print(f"Total Pages: {len(pdfReader.pages)}")

# Get the first page object
pageObj = pdfReader.pages[0]

# Extract text from the page
print(pageObj.extract_text())

# Close the pdf file object
pdfFileObj.close()
