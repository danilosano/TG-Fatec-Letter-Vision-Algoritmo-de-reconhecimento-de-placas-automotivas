import cv2
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


placasXml = 'br.xml'
placasCascade = cv2.CascadeClassifier(placasXml)

# path = "images"
# dirs = os.listdir( path )

Text = ""
imagemInput = cv2.imread('placaSimples.jpg')
hImg, wImg, _ = imagemInput.shape

faces = placasCascade.detectMultiScale(
        imagemInput,
        minNeighbors=20,
        minSize=(30, 30),
	    maxSize=(300,300)
    )

for (x, y, w, h) in faces:

    cv2.rectangle(imagemInput, (x, y), (x+w, y+h), (0, 255, 0), 4)
    boximg = pytesseract.image_to_boxes(imagemInput)
    
    for b in boximg.splitlines():
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        Text += b[0]
        cv2.rectangle(imagemInput, (x, hImg - y), (w, wImg - h), (50, 50, 255), 1)
        
print(Text)

# acertos = 0
# erros = 0
# # cont = 0
# contText = str(cont)
# acertosText = str(acertos)
# errosText = str(erros)
# print("Total de arquivos percorridos:" + contText + "\nTotal de acertos: " + acertosText +"\nTotal de erros: " + errosText)

cv2.imshow('Detected text', imagemInput)
cv2.waitKey(0)

