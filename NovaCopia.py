import pandas as pd
import os
import shutil

# Ler o arquivo Excel
df = pd.read_excel('Pasta5.xlsx')

# Iterar sobre as linhas do DataFrame
for index, row in df.iterrows():
    # Obter o caminho completo do arquivo original da coluna "Diretório e Nome Original"
    caminho_original = row['a']

    # Obter o novo nome da coluna "Nome da Cópia"
    novo_nome = row['b']

    # Obter o diretório do arquivo original
    diretorio = os.path.dirname(caminho_original)

    # Montar o caminho completo do novo arquivo
    caminho_novo = os.path.join(diretorio, novo_nome)

    try:
        # Criar uma cópia do arquivo com o novo nome
        shutil.copy2(caminho_original, caminho_novo)
        print(f"Cópia criada: {caminho_original} -> {caminho_novo}")
    except Exception as e:
        print(f"Erro ao criar cópia do arquivo {caminho_original}: {str(e)}")
