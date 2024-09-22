import os
import cv2
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Diretórios para as imagens de treinamento
diretorio_manuscrito = 'C:/bancos/baseDfotos/treinamento/manuscrito'
diretorio_impresso = 'C:/bancos/baseDfotos/treinamento/impresso'

# Carregar imagens de treinamento e atribuir rótulos
dados_treinamento = []
rótulos_treinamento = []

# Carregar imagens manuscritas e atribuir rótulo 0
for arquivo in os.listdir(diretorio_manuscrito):
    if arquivo.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        caminho_imagem = os.path.join(diretorio_manuscrito, arquivo)
        imagem = cv2.imread(caminho_imagem)
        imagem = cv2.resize(imagem, (150, 150))  # Redimensione a imagem conforme necessário
        dados_treinamento.append(imagem)
        rótulos_treinamento.append(0)  # Rótulo 0 para "manuscrito"

# Carregar imagens impressas e atribuir rótulo 1
for arquivo in os.listdir(diretorio_impresso):
    if arquivo.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        caminho_imagem = os.path.join(diretorio_impresso, arquivo)
        imagem = cv2.imread(caminho_imagem)
        imagem = cv2.resize(imagem, (150, 150))  # Redimensione a imagem conforme necessário
        dados_treinamento.append(imagem)
        rótulos_treinamento.append(1)  # Rótulo 1 para "impresso"

# Converter dados e rótulos em arrays NumPy
dados_treinamento = np.array(dados_treinamento)
rótulos_treinamento = np.array(rótulos_treinamento)

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
modelo.save('modelo_treinado.h5')
