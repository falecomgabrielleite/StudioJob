import cv2
import numpy as np
import pytesseract
import os

def read_image(image_path):
  image = cv2.imread(image_path)
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
  return image

def extract_text(image):
  text = pytesseract.image_to_string(image)
  return text

def train_model(reference_images, manuscript_images):
  reference_texts = []
  manuscript_texts = []
  for reference_image in reference_images:
    reference_text = extract_text(reference_image)
    reference_texts.append(reference_text)
  for manuscript_image in manuscript_images:
    manuscript_text = extract_text(manuscript_image)
    manuscript_texts.append(manuscript_text)

  model = pytesseract.create()
  model.train(reference_texts, manuscript_texts)
  return model

def identify_letters(model, manuscript_image):
  text = extract_text(manuscript_image)
  letters = []
  for character in text:
    letter = model.get_character_from_string(character)
    letters.append(letter)
  return letters

if __name__ == '__main__':
  # Read the reference images.
  reference_images = []
  for file in os.listdir('C:/bancos/baseDfotos/treinamento/impresso/'):
    if file.endswith('.png'):
      reference_images.append(os.path.join('C:/bancos/baseDfotos/treinamento/impresso/', file))

  # Read the manuscript images.
  manuscript_images = []
  for file in os.listdir('C:/bancos/baseDfotos/treinamento/manuscrito/'):
    if file.endswith('.png'):
      manuscript_images.append(os.path.join('C:/bancos/baseDfotos/treinamento/manuscrito/', file))

  # Train the model.
  model = train_model(reference_images, manuscript_images)

  # Identify the letters in the manuscript image.
  manuscript_image = read_image('C:/bancos/baseDfotos/treinamento/manuscrito/escrita.png')
  letters = identify_letters(model, manuscript_image)

  # Print the result.
  for letter in letters:
    print(letter)
