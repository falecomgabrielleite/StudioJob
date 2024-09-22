import os
import openpyxl

# Caminho para o diretório onde os arquivos estão localizados
diretorio_arquivos = 'C:/bancos/brandili_2024/'

# Caminho para o arquivo Excel com os nomes de renomeação
caminho_planilha_excel = 'C:/bancos/brandili_2024/planilhaMestre.xlsx'

# Carregar a planilha Excel
workbook = openpyxl.load_workbook(caminho_planilha_excel)
sheet = workbook.active

# Mapear os nomes atuais para os novos nomes a partir da planilha
mapeamento_nomes = {}
for row in sheet.iter_rows(min_row=2, values_only=True):
    nome_atual, novo_nome = row
    mapeamento_nomes[nome_atual] = novo_nome

# Iterar sobre os arquivos no diretório
for arquivo in os.listdir(diretorio_arquivos):
    if arquivo in mapeamento_nomes:
        novo_nome = mapeamento_nomes[arquivo]
        caminho_antigo = os.path.join(diretorio_arquivos, arquivo)
        caminho_novo = os.path.join(diretorio_arquivos, novo_nome)

        # Renomear o arquivo
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {arquivo} -> {novo_nome}")

# Fechar a planilha Excel
workbook.close()
