import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('alo.jpg')
img = cv2.resize(img, (720, 480))

hImg, wImg, _ = img.shape

boximg = pytesseract.image_to_boxes(img)
chars = boximg.splitlines()

lenght = len(chars)

print(chars[4])
Text = ""
for b in boximg.splitlines():
  b = b.split(' ')
  x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])

  Text += b[0]
  cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 1)
  cv2.putText(img, b[0], (x, hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)

print(Text)
cv2.imshow('Detected text', img)
cv2.waitKey(0)