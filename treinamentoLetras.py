import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Suponhamos que você tenha uma estrutura de diretório com pastas 'manuscrito' e 'impresso' contendo as imagens
diretorio_treinamento = 'C:/bancos/baseDfotos/treinamento/'
diretorio_validacao = 'C:/bancos/baseDfotos/validacao/'

# Pré-processamento de imagens
datagen = ImageDataGenerator(rescale=1.0/255.0) # Normalização dos pixels

tamanho_lote = 32

# Carregando dados de treinamento e validação
gerador_treinamento = datagen.flow_from_directory(
    diretorio_treinamento,
    target_size=(150, 150),  # Redimensione todas as imagens para o mesmo tamanho
    batch_size=tamanho_lote,
    class_mode='binary'  # Classificação binária (manuscrito ou impresso)
)

gerador_validacao = datagen.flow_from_directory(
    diretorio_validacao,
    target_size=(150, 150),
    batch_size=tamanho_lote,
    class_mode='binary'
)

# Definindo a arquitetura do modelo
modelo = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Camada de saída para classificação binária
])

# Compilando o modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Treinando o modelo
historico = modelo.fit(
    gerador_treinamento,
    steps_per_epoch=len(gerador_treinamento),
    epochs=10,
    validation_data=gerador_validacao,
    validation_steps=len(gerador_validacao)
)

# Avaliando o modelo
resultado = modelo.evaluate(gerador_validacao)

# Salvar o modelo treinado em um arquivo .h5
modelo.save('modelo_treinado.h5')

print("Acurácia no conjunto de validação:", resultado[1])
