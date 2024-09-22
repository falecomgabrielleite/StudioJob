import pytesseract
from PIL import Image

# Caminho da imagem .jpg
image_path = 'C:/bancos/baseDfotos/feminino8.jpg'

# Carregar a imagem
img = Image.open(image_path)

# Extrair texto da imagem
text = pytesseract.image_to_string(img)

# Imprimir o texto extraído
print(text)
