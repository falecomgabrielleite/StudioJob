import os
from PIL import Image
import pytesseract

# Diretório onde as imagens estão localizadas
diretorio_imagens = 'C:/bancos/baseDfotos/treinamento'

# Configuração do caminho do executável do Tesseract (altere de acordo com o seu sistema)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Percorrer todas as imagens no diretório
for nome_arquivo in os.listdir(diretorio_imagens):
    if nome_arquivo.endswith('.png') or nome_arquivo.endswith('.jpg') or nome_arquivo.endswith('.jpeg'):
        caminho_completo = os.path.join(diretorio_imagens, nome_arquivo)

        # Carregar a imagem usando PIL
        imagem = Image.open(caminho_completo)

        # Reconhecer o texto na imagem usando Tesseract
        texto_encontrado = pytesseract.image_to_string(imagem)

        # Remover caracteres não alfanuméricos do texto (para usar como nome do arquivo)
        nome_novo_arquivo = ''.join(c for c in texto_encontrado if c.isalnum() or c.isspace())

        # Renomear o arquivo com o texto encontrado
        novo_caminho_completo = os.path.join(diretorio_imagens, f'{nome_novo_arquivo}.jpg')

        # Renomear o arquivo
        os.rename(caminho_completo, novo_caminho_completo)

        print(f'Arquivo renomeado: {nome_arquivo} -> {nome_novo_arquivo}.jpg')
