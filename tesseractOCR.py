import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(Image.open('img1.jpg'))
print(text)
