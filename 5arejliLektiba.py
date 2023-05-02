import cv2
img = cv2.imread('1.png')
import easyocr

reader = easyocr.Reader(['fr'], gpu=False)

result = reader. readtext(img)
for text in result:

    detctedText = text [1]
    print (detctedText)
