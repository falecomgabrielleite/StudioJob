import os
import cv2
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Diretório para as imagens de treinamento
diretorio_manuscrito = 'C:/bancos/baseDfotos/treinamento/manuscrito/'
diretorio_impresso = 'C:/bancos/baseDfotos/treinamento/impresso/'

# Função para carregar e pré-processar as imagens
def carregar_e_preprocessar_imagens(diretorio):
    dados = []
    rótulos = []
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            caminho_imagem = os.path.join(diretorio, arquivo)
            imagem = cv2.imread(caminho_imagem)
            imagem = cv2.resize(imagem, (150, 150))  # Redimensione a imagem conforme necessário
            imagem = imagem / 255.0  # Normalização dos pixels (0-1)
            dados.append(imagem)
            if "manuscrito" in diretorio:
                rótulos.append(0)  # Rótulo 0 para manuscrito
            elif "impresso" in diretorio:
                rótulos.append(1)  # Rótulo 1 para impresso
    return np.array(dados), np.array(rótulos)

# Carregar imagens de treinamento
dados_manuscrito, rótulos_manuscrito = carregar_e_preprocessar_imagens(diretorio_manuscrito)
dados_impresso, rótulos_impresso = carregar_e_preprocessar_imagens(diretorio_impresso)

# Concatenar dados e rótulos
dados_treinamento = np.concatenate([dados_manuscrito, dados_impresso])
rótulos_treinamento = np.concatenate([rótulos_manuscrito, rótulos_impresso])

# Construir o modelo
modelo = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Compilar o modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Treinar o modelo
modelo.fit(dados_treinamento, rótulos_treinamento, epochs=10)

# Salvar o modelo treinado em um arquivo .h5
modelo.save('modelo_ocr.h5')
