import os, cv2, mahotas, pytesseract, time
from PIL import Image



img = cv2.cvtColor(imagemInput, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (3, 3), 10)
T = mahotas.thresholding.otsu(suave)
