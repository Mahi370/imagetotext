import pytesseract
from PIL import Image


img = Image.open('image.jpg')
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
result = pytesseract.image_to_string(img)

with open('magic.txt',mode='w') as file:
    file.write(result)
    print('>see the magic file dude!')