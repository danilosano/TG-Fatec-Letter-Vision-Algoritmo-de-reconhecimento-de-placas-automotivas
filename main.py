import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Até aqui eu só mexi nas config e import


# Aqui eu li a imagem alo.jpg com o cv2 e coloquei ela na variavel ali, depois só mudei o tamnho dela pra 720x480
img = cv2.imread('alo.jpg')
img = cv2.resize(img, (720, 480))

#Criando variavel aqui de tamanho pegando da imagem
hImg, wImg, _ = img.shape

# Esse image to boxes corta as letras que ele acha que achou e coloca numa variavel
boximg = pytesseract.image_to_boxes(img)

# Variavel onde vai ficar a string da placa ou do que ele le, começa vazio pq obviamente né k
Text = ""

# Aqui ele vai percorrendo todos os retangulos que ele achou, cada retangula tem na ordem [LETRA, POS X, POS Y, 
# POS DIAGONAL X???, POS DIAGONAL Y???]
for b in boximg.splitlines():
  b = b.split(' ')
  x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
# Aqui ele coloca as letras uma por uma na variavel da placa

  Text += b[0]

# Aqui ele enquadra o retangulo em volta da letra que ele tinha achado
  cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 1)
# Aqui ele só desenha o retangulo e escreve a letra que ele achou em baixo do retangulo
  cv2.putText(img, b[0], (x, hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)

# Escreve a variavel no consolezinho
print(Text)

# Mostra a imagem na janela que abriu
cv2.imshow('Detected text', img)

# Ta esperando se apertar 0 pra fechar, enquanto n aperta ele fica funcionando
cv2.waitKey(0)