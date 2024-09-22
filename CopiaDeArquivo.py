import pandas as pd
import os
import shutil

# Ler o arquivo Excel
df = pd.read_excel('renomear-dia22.xlsx')

# Iterar sobre as linhas do DataFrame
for index, row in df.iterrows():
    # Obter o diretório e o nome do arquivo original da coluna "Diretório"
    diretorio = row['a']
    nome_original = row['b']

    # Obter o novo nome da coluna "Nome que o programa em Python deve renomear"
    novo_nome = row['c']

    # Montar o caminho completo do arquivo original
    caminho_original = os.path.join(diretorio, nome_original)

    # Montar o caminho completo do novo arquivo
    caminho_novo = os.path.join(diretorio, novo_nome)

    try:
        # Criar uma cópia do arquivo com o novo nome
        shutil.copy2(caminho_original, caminho_novo)
        print(f"Cópia criada: {caminho_original} -> {caminho_novo}")
    except Exception as e:
        print(f"Erro ao criar cópia do arquivo {caminho_original}: {str(e)}")
