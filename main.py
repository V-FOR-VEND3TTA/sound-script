# Import the text to speech and pdf reader modules
import pyttsx3
import PyPDF2
from PyPDF2 import PdfReader

book = open('Blitzscaling by Reid Hoffman, Chris Yeh.pdf', 'rb')
reader = PdfReader(book)

# Checking the number of pages the book contains
pages = len(reader.pages)
print('This ebook has', pages, 'pages')


# using our device speakers and the pyttsx3 module
speaker = pyttsx3.init()

# loop through this ebook from the second page
for num in range(1, pages):
    page = reader.pages[40]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait() # stop after saying something

