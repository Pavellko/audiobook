import pyttsx3
import PyPDF2
import find
book = open('Clifford D Simak - The Visitors - 1980.pdf', 'rb')

print(find.findi())

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

# speaker = pyttsx3.init()

# for num in range(2, pages):
#     page = pdfReader.getPage(num)
#     text = page.extractText()
#     speaker.say(text)
#     speaker.runAndWait()

engine = pyttsx3.init()
voice = engine.getProperty('voices')
zx={}
for i in voice:
    zx[i.name] = i.id
    
print(zx.items())



engine.setProperty('voice', zx['Microsoft David Desktop - English (United States)'])


p = pdfReader.getPage(19)
txt = p.extractText()

engine.say(txt)
engine.runAndWait()

