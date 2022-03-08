import cv2
import pytesseract
cv2.CascadeClassifier
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

arqCasc1 = 'br.xml'
faceCascade1 = cv2.CascadeClassifier(arqCasc1) #classificador para o rosto
hImg = 1080
wImg = 1920
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  #instancia o uso da webcam


while True:
    s, imagem = webcam.read() #pega efeticamente a imagem da webcam
    
    #Aqui ele só pega as placas, ta com nome de face mas é pq eu so reutilizei o codigo do reconhecimento facial
    faces = faceCascade1.detectMultiScale(
        imagem,
        minNeighbors=20,
        minSize=(30, 30),
	maxSize=(300,300)
        
    )

    #Aqui eu reaproveite que toda vez que ele acha um quadrado da placa ele le, pra n ficar lendo a toa toda hora
    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 4) #escreve o retangulo em volta da placa
        boximg = pytesseract.image_to_boxes(imagem) #divide e lê os caracteres que ele achou na imagem
        Text = ""
        for b in boximg.splitlines(): #for pra percorrer todas as letras que ele achou e vai sair desenhando e escrevendo tudo
            b = b.split(' ')
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            Text += b[0]
            cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 4) #coloca um retangulo em volta das letras
            cv2.putText(imagem, b[0], (x, hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)#aparece as letras na imagem da camera
        print(Text)
    

    cv2.imshow('Video', imagem) #mostra a imagem captura na janela

    #o trecho seguinte e apenas para parar o codigo e fechar a janela
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release() #dispensa o uso da webcam
cv2.destroyAllWindows() #fecha todas a janelas abertas
