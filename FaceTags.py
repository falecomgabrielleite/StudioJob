import cv2

# Carregar a imagem
image_path = 'C:/bancos/baseDfotos/feminino8.jpg'
image = cv2.imread(image_path)

# Converter para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Carregar o classificador Haar Cascade para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detectar rostos na imagem
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Mostrar o resultado
if len(faces) > 0:
    model_detected = True
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Salvar a imagem com detecções
    output_path = '/mnt/data/detected_image.jpg'
    cv2.imwrite(output_path, image)
    print(f"Modelo humano detectado na imagem. Imagem salva em {output_path}")
else:
    model_detected = False
    print("Nenhum modelo humano detectado na imagem.")
