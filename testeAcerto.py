import cv2
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

placasXml = 'br.xml'
placasCascade = cv2.CascadeClassifier(placasXml)

path = "images"
dirs = os.listdir( path )

acertos = 0
erros = 0
cont = 0

for item in dirs:
    cont += 1
    Text = ""
    imagemInput = cv2.imread("images/"+item)
    nomeArquivoAtual = item.replace('.jpg', '')
    nomeArquivoAtual = nomeArquivoAtual.replace('.JPG', '')
    nomeArquivoAtual = nomeArquivoAtual.replace('-', '')

    hImg, wImg, _ = imagemInput.shape

    faces = placasCascade.detectMultiScale(
            imagemInput,
            minNeighbors=20,
            minSize=(30, 30),
            maxSize=(300,300)
        )

    for (x, y, w, h) in faces:
        boximg = pytesseract.image_to_boxes(imagemInput)
        for b in boximg.splitlines():
            b = b.split(' ')
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            Text += b[0]
            
    Text = Text.replace('~', '')
    Text = Text.replace('-', '')
    Text = Text.replace(':', '')
    if(Text.find(nomeArquivoAtual) > -1):
        acertos += 1
    else:
        erros += 1

TaxaAcerto = acertos/cont*100
TaxaErro = erros/cont*100

contText = str(cont)
TaxaAcerto = str(TaxaAcerto)
TaxaErro = str(TaxaErro)
print("Total de arquivos percorridos:" + contText + "\nTotal de acertos: " + TaxaAcerto +"%\nTotal de erros: " + TaxaErro+"%")


