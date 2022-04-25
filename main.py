from matplotlib import pyplot as plt
import cv2 , pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

img = cv2.imread('imagemSimples.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converte P&B
blurred = cv2.GaussianBlur(img, (5,5), 0)
mid = cv2.Canny(blurred, 105, 140)

cv2.imshow("Imagem P&B", mid)
cv2.waitKey(0)
