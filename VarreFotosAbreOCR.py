import json
import os
import requests
import pandas as pd

# Fornecer seu nome de usuário e código de licença
LicenseCode = 'B2D05D47-9CEE-4BF2-88AF-14BA79E01D4C'
UserName = 'MOREIRAGNOMOX'

# URL da API do OCRWebService.com
RequestUrl = "http://www.ocrwebservice.com/restservices/processDocument?gettext=true"

# Caminho para a pasta raiz contendo todas as subpastas
root_folder = "C:/bancos/baseDfotos/TAGS"

# Lista para armazenar os dados do OCR
ocr_data = []

# Função para percorrer recursivamente todas as subpastas e buscar arquivos de imagem
def search_images(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for filename in files:
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                # Caminho completo do arquivo
                image_path = os.path.join(root, filename)

                # Lendo o conteúdo da imagem
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

                # Adicionar os dados do OCR à lista
                ocr_data.append({'Caminho do Arquivo': image_path, 'Texto Extraído': extracted_text})

# Verificar se a pasta raiz existe
if os.path.exists(root_folder):
    # Chamar a função para percorrer recursivamente todas as subpastas e buscar arquivos de imagem
    search_images(root_folder)

    # Criar DataFrame a partir dos dados do OCR
    df_report = pd.DataFrame(ocr_data)

    # Salvar DataFrame como arquivo Excel na pasta C:/bancos/baseDfotos/
    report_path = os.path.join("C:/bancos/baseDfotos/", "reportOCR.xlsx")
    df_report.to_excel(report_path, index=False)

    print(f"Relatório do OCR salvo em: {report_path}")
else:
    print("A pasta raiz especificada não existe.")
