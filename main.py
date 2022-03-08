import cv2
import pytesseract
cv2.CascadeClassifier
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

arqCasc1 = 'br.xml'
faceCascade1 = cv2.CascadeClassifier(arqCasc1)
hImg = 1080
wImg = 1920
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW) 


while True:
    s, imagem = webcam.read() 
    
    faces = faceCascade1.detectMultiScale(
        imagem,
        minNeighbors=20,
        minSize=(30, 30),
	maxSize=(300,300)
        
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 4)
        boximg = pytesseract.image_to_boxes(imagem)
        Text = ""
        for b in boximg.splitlines():
            b = b.split(' ')
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            Text += b[0]
            cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 4)
            cv2.putText(imagem, b[0], (x, hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)
        print(Text)
    

    cv2.imshow('Video', imagem) 


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
