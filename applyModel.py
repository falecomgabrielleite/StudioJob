import os
from PIL import Image
import pytesseract
from tensorflow import keras

# Carregar o modelo treinado
modelo = keras.models.load_model('modelo_ocr.h5')

# Diretório de validação
diretorio_validacao = 'C:/bancos/baseDfotos/treinamento/'

# Configuração do caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Substitua pelo seu caminho

for pasta in os.listdir(diretorio_validacao):
    pasta_path = os.path.join(diretorio_validacao, pasta)
    if os.path.isdir(pasta_path):
        for arquivo in os.listdir(pasta_path):
            arquivo_path = os.path.join(pasta_path, arquivo)
            if arquivo.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # Carregar a imagem
                imagem = Image.open(arquivo_path)

                # Pré-processamento (redimensionar, normalizar, etc., se necessário)

                # Realizar OCR na imagem
                texto = pytesseract.image_to_string(imagem)

                # Imprimir o texto extraído
                print(f'Arquivo: {arquivo_path}')
                print(f'Texto Extraído: {texto}\n')
