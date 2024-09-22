import json
import os
import requests
import pandas as pd

# Fornecer seu nome de usuário e código de licença
LicenseCode = '3CE8CB65-1DBF-454A-9A57-DB7CC840506E'
UserName = 'gabrielleite'

# URL da API do OCRWebService.com
RequestUrl = "http://www.ocrwebservice.com/restservices/processDocument?gettext=true"

# Caminho para a planilha reportTags.xlsx
tags_excel_path = "C:/bancos/baseDfotos/reportTags.xlsx"

# Lista para armazenar os dados do OCR
ocr_data = []

# Função para processar o OCR em imagens e atualizar a planilha
def process_ocr_and_update_sheet(tags_excel_path):
    # Carregar a planilha
    df_tags = pd.read_excel(tags_excel_path)

    # Percorrer cada linha da planilha
    for index, row in df_tags.iterrows():
        # Obter o caminho do arquivo de imagem da coluna C
        image_path = row['Caminho Completo']

        # Ler o conteúdo da imagem
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        # Enviar a imagem para a API e obter a resposta
        response = requests.post(RequestUrl, data=image_data, auth=(UserName, LicenseCode))

        if response.status_code == 401:
            # Fornecer nome de usuário e código de licença válidos
            print("Solicitação não autorizada")
            exit()

        # Decodificar a resposta JSON
        jobj = json.loads(response.content)

        ocrError = str(jobj["ErrorMessage"])

        if ocrError != '':
            # Ocorreu um erro durante o reconhecimento
            print("Erro de reconhecimento: " + ocrError)
            exit()

        # Texto extraído da primeira página
        extracted_text = str(jobj["OCRText"][0][0])

        # Atualizar a coluna D correspondente com o texto extraído
        df_tags.at[index, 'Texto Extraído'] = extracted_text

    # Salvar a planilha atualizada
    df_tags.to_excel(tags_excel_path, index=False)
    print(f"Texto extraído e atualizado em {tags_excel_path}")

# Verificar se o arquivo da planilha existe
if os.path.exists(tags_excel_path):
    # Chamar a função para processar o OCR e atualizar a planilha
    process_ocr_and_update_sheet(tags_excel_path)
else:
    print("O arquivo da planilha especificado não existe.")
