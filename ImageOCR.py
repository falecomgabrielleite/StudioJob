import requests
import base64  # Adicione esta linha

# URL da API do OCR.Space
api_url = 'https://api.ocr.space/parse/image'

# Chave de API (substitua 'SUA_CHAVE_DE_API' pela sua chave real)
api_key = 'K81339242988957'

# Caminho da imagem .jpg que você deseja extrair texto
image_path = 'C:/bancos/baseDfotos/feminino8.jpg'

# Parâmetros da solicitação
payload = {
    'apikey': api_key,
    'language': 'por',  # Idioma da imagem (ajuste conforme necessário)
    'isOverlayRequired': False,
    'base64Image': True,
}

# Enviar a imagem para a API e obter a resposta
with open(image_path, 'rb') as f:
    # Codificar a imagem em base64
    base64_image = base64.b64encode(f.read()).decode('utf-8')
    payload['base64Image'] = 'data:image/jpeg;base64,' + base64_image

    # Enviar a solicitação POST para a API
    response = requests.post(api_url, data=payload)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Extrair texto da resposta JSON
    json_response = response.json()
    print(json_response)  # Exibe a resposta JSON completa para análise
else:
    print(f'Erro ao enviar solicitação para API. Código de status: {response.status_code}')