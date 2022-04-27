import qrcode

#o que vai ser imprimido no qrcode
data = 'Teste de criacao de qrcode'

img = qrcode.make(data)

#local aonde sera salvo o qrcode
img.save('C:/Users/Juca/OneDrive/Documentos/Qrcode/meuqrcode.png')