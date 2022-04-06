import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('images/AXX-1773.jpg')
img = cv2.resize(img, (720, 480))

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

boximg = pytesseract.image_to_string(th3)
chars = boximg.splitlines()
lenght = len(chars)

Text = boximg

print(Text)
cv2.imshow('Detected text', th3)
cv2.waitKey(0) 