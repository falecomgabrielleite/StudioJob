import easyocr

# Caminho da imagem .jpg
image_path = 'C:/bancos/baseDfotos/feminino8.jpg'

# Inicializar o objeto EasyOCR
reader = easyocr.Reader(['en'])  # 'en' para inglês, ajuste conforme necessário

# Extrair texto da imagem
result = reader.readtext(image_path)

# Imprimir o texto extraído
for detection in result:
    print(detection[1])
