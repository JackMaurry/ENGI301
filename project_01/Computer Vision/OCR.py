# installations completed
#sudo apt install tesseract-ocr

import pytesseract
from pytesseract import Output
from PIL import Image

img_path1 = 'Images/Jack_Spades_TestImg.png'
text = pytesseract.image_to_string(Image.open(img_path1),lang='eng')
print(text)
