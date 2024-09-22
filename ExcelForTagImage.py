import os
import cv2
import pytesseract
import pandas as pd

# Configurar o caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'


# Função para pré-processar a imagem e detectar texto (focado em números)
def detect_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar um filtro adaptativo para melhorar o contraste
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Rotacionar a imagem para a direita
    rotated = cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE)

    # Usar Tesseract para detectar texto, focando em números
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    text = pytesseract.image_to_string(rotated, config=custom_config).strip()

    return text


# Caminhos
base_folder = 'C:/bancos/baseDfotos'
excel_path = os.path.join(base_folder, 'teste.xlsx')

# Carregar o arquivo Excel e ler a coluna A
df = pd.read_excel(excel_path)
column_a_values = df.iloc[:, 0].astype(str).tolist()

# Percorrer todas as imagens na pasta
for filename in os.listdir(base_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Ajuste conforme necessário
        image_path = os.path.join(base_folder, filename)
        print(f'Processando imagem: {filename}')

        # Detectar texto na imagem
        detected_text = detect_text(image_path)
        print(f'Texto detectado na imagem {filename}: {detected_text}')

        # Procurar os valores da coluna A no texto detectado
        matched_value = next((value for value in column_a_values if value.lower() in detected_text.lower()), None)

        if matched_value:
            # Usar o valor encontrado para renomear o arquivo
            new_name = matched_value
            print(f'Texto correspondente encontrado: {new_name}')
            new_image_path = os.path.join(base_folder, f'{new_name}.jpg')

            if not os.path.exists(new_image_path):
                os.rename(image_path, new_image_path)
                print(f'Imagem renomeada para: {new_image_path}')
            else:
                print(f'Arquivo {new_image_path} já existe. Pulando...')

print("Processamento concluído.")
