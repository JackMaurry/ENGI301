# installations completed
#sudo apt install tesseract-ocr

import pytesseract
from pytesseract import Output
from PIL import Image
import numpy as np

img_path1 = 'Images/Ace_TestImg.png'
#img_path1 = 'Images/RealPhotoTestImg.png'
#img_path1 = 'Images/Jack_Spades_TestImg.png'
#img_path1 = 'Images/test8.png'

# resizes and greyscales the image. if you include the crop without some hearts 
# itll cooperate with the 8 image and not include the period "8." before the jibberish filter
img = Image.open(img_path1).convert("L").resize((256, 256)).crop((0,0,200,200)) 
img = np.array(img) # converts the image to a pixel array
img = (img > 150).astype("uint8") * 255 # converts the image to a binary representation, 255 if its above 150 and 0 if its less
Image.fromarray(img).save("Images/out.png") # verifies that the binary output is good
# Note: conversion is really important for increasing result quality in pytesseract
text = pytesseract.image_to_string(img, lang='eng', config='--psm 10') 
# uses the psm 10 argument to specify "sparse text" which will recognize individual chars
#print("Before jibberish filter:", text)
 # jibberish filter for good measure. If the output of pytesseract is "1O" or "8." or anything weird it'll try to handle it.
if len(text) >= 2 and text[:2] in ("10", "1O"):
    text = "10" # makes the text 10
elif len(text) >= 1:
    text = text[0] # takes the first character
print(text)
# print(img)
# print(sum(img == 255))
# print(img.shape)
