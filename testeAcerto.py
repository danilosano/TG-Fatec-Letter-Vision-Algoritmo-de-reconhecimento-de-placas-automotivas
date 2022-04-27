import cv2, pytesseract, os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

placasXml = 'br.xml'
placasCascade = cv2.CascadeClassifier(placasXml)

path = "images"
dirs = os.listdir( path )

acertos = 0
erros = 0
contTotal = 0
cont = 0

for item in dirs:
    contTotal += 1
    Text = ""
    imagemInput = cv2.imread("images/"+item)    
    nomeArquivoAtual = item.replace('.jpg', '')    
    nomeArquivoAtual = nomeArquivoAtual.replace('.JPG', '')
    nomeArquivoAtual = nomeArquivoAtual.replace('-', '')
    nomeArquivoAtual = nomeArquivoAtual.replace('(1)', '')
    nomeArquivoAtual = nomeArquivoAtual.replace('(2)', '')
    nomeArquivoAtual = nomeArquivoAtual.replace('-1', '')
    nomeArquivoAtual = nomeArquivoAtual.replace('-2', '')

    imagemInput = cv2.cvtColor(imagemInput, cv2.COLOR_BGR2GRAY)
    imagemInput = cv2.GaussianBlur(imagemInput, (9,9), 0)

    placas = placasCascade.detectMultiScale(
            imagemInput,
            scaleFactor=1.05,
            minNeighbors=5,
            minSize=(30, 30)
        )

    for (x, y, w, h) in placas:
        cont += 1
        recortePlaca = imagemInput[y:y + h, x:x + w]

        Text = pytesseract.image_to_string(recortePlaca)

        Text = Text.replace('~', '')
        Text = Text.replace('-', '')
        Text = Text.replace(':', '')
        Text = Text.replace('!', '')
        Text = Text.replace(' ', '')
        Text = Text.replace('`', '')
        Text = Text.replace('|', '')
        Text = Text.replace('.', '')
        Text = Text.replace('‘', '')
        Text = Text.replace('/', '')
        Text = Text.replace('>', '')
        Text = Text.replace('<', '')
        print(Text + " foi o texto achado na placa:"+ nomeArquivoAtual)
        if(Text.find(nomeArquivoAtual) > -1):
            acertos += 1
        else:
            erros += 1

TaxaAcerto = acertos/cont*100
TaxaErro = erros/cont*100

contTotalText = str(contTotal)
contText = str(cont)
TaxaAcerto = str(TaxaAcerto)
TaxaErro = str(TaxaErro)
print("Total de arquivos percorridos:" + contTotalText +"\nTotal de placas encontradas:" + contText + 
"\nTotal de acertos: " + TaxaAcerto +
"%\nTotal de erros: " + TaxaErro+"%")
cv2.waitKey(0)