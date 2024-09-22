import os
import pytesseract
from PIL import Image

# Defina o caminho para o diretório
diretorio = 'C:/bancos/baseDfotos/'

# Configuração do caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Substitua pelo seu caminho

# Coordenadas da área de interesse (ROI) na imagem
x1, y1 = 2000, 471  # Canto superior esquerdo
x2, y2 = 2700, 1104   # Canto inferior direito

# Loop pelos arquivos no diretório
for arquivo in os.listdir(diretorio):
    caminho_completo = os.path.join(diretorio, arquivo)
    if os.path.isfile(caminho_completo):
        # Verifica se o arquivo é uma imagem (você pode ajustar as extensões conforme necessário)
        if caminho_completo.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Abra a imagem
            imagem = Image.open(caminho_completo)

            # Recorte a área de interesse (ROI)
            roi = imagem.crop((x1, y1, x2, y2))

            # Realize OCR na área de interesse (ROI)
            texto = pytesseract.image_to_string(roi)

            # Imprime o texto extraído
            print(f'Arquivo: {caminho_completo}')
            print(f'Texto Extraído na Área de Interesse: {texto}\n')
