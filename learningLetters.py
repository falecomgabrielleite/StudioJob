import os
import cv2
import numpy as np
from tensorflow import keras

# Diretórios para as pastas Manuscrito e Impresso
diretorio_manuscrito = 'C:/bancos/baseDfotos/treinamento/manuscrito'
diretorio_impresso = 'C:/bancos/baseDfotos/treinamento/impresso'

# Função para carregar e pré-processar uma única imagem
def carregar_e_preprocessar_imagem(caminho_imagem):
    imagem = cv2.imread(caminho_imagem)
    imagem = cv2.resize(imagem, (150, 150))  # Redimensione a imagem conforme necessário
    imagem = imagem / 255.0  # Normalização dos pixels (0-1)
    return imagem

# Carregar o modelo treinado
modelo = keras.models.load_model('modelo_ocr.h5')

# Carregar a imagem de caligrafia manual
caminho_manuscrito = os.path.join(diretorio_manuscrito, 'escrita.png')
imagem_manuscrito = carregar_e_preprocessar_imagem(caminho_manuscrito)

# Realizar a previsão no manuscrito
previsao = modelo.predict(np.array([imagem_manuscrito]))

# Se o valor previsto estiver próximo de 0, é mais provável que seja caligrafia manual
if previsao[0] < 0.5:
    print("A imagem é caligrafia manual.")
else:
    print("A imagem é impressa.")
