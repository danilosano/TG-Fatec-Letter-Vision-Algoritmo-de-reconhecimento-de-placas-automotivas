import pytesseract, cv2, mahotas
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

img = cv2.imread('placaSimples.jpg')

hImg, wImg, _ = img.shape

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (3, 3), 10)
T_otsu = mahotas.thresholding.otsu(suave)

cv2.imshow(img >T_otsu))
cv2.waitKey(0) 