import os
import openpyxl

# Diretório que você deseja listar
diretorio_arquivos = 'C:/bancos/novas/Desconjuntado'

# Nome do arquivo Excel a ser criado
nome_arquivo_excel = 'arquivoDesconjuntado_1810.xlsx'

# Inicializar um novo arquivo Excel
workbook = openpyxl.Workbook()
sheet = workbook.active

# Listar os arquivos no diretório e escrever seus nomes na coluna A
for idx, arquivo in enumerate(os.listdir(diretorio_arquivos), start=1):
    sheet.cell(row=idx, column=1, value=arquivo)

# Salvar o arquivo Excel
caminho_excel = os.path.join(diretorio_arquivos, nome_arquivo_excel)
workbook.save(caminho_excel)

# Fechar o arquivo Excel
workbook.close()

print(f'O arquivo Excel foi criado em: {caminho_excel}')
