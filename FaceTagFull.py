import os
import cv2
import pytesseract
import pandas as pd

# Configurar o caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'


# Função para detectar texto na imagem
def detect_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='por')  # Ajuste o idioma conforme necessário
    return text.strip()


# Função para detectar rostos na imagem
def detect_faces(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return len(faces) > 0


# Caminhos
base_folder = 'C:/bancos/baseDfotos'
excel_path = os.path.join(base_folder, 'teste.xlsx')

# Carregar o arquivo Excel
df = pd.read_excel(excel_path)

# Percorrer todas as imagens na pasta
for filename in os.listdir(base_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Ajuste conforme necessário
        image_path = os.path.join(base_folder, filename)

        # Detectar texto na imagem
        detected_text = detect_text(image_path)
        print(f'Texto detectado na imagem {filename}: {detected_text}')

        # Encontrar texto no Excel
        match = df[df.apply(lambda row: detected_text.lower() in str(row).lower(), axis=1)]

        if not match.empty:
            # Usar o valor da coluna A para renomear o arquivo
            new_name = match.iloc[0, 0]
            print(f'Texto encontrado no Excel: {new_name}')
            new_image_path = os.path.join(base_folder, f'{new_name}.jpg')

            if not os.path.exists(new_image_path):
                os.rename(image_path, new_image_path)
                print(f'Imagem renomeada para: {new_image_path}')
            else:
                print(f'Arquivo {new_image_path} já existe. Pulando...')

            # Verificar a presença de modelo humano
            if detect_faces(new_image_path):
                final_image_path = os.path.join(base_folder, f'{new_name}.1.jpg')
                os.rename(new_image_path, final_image_path)
                print(f'Imagem com modelo humano renomeada para: {final_image_path}')

print("Processamento concluído.")
