#CODIGO COMPATIBLE CON GOOGLE COLAB

# Instalar face_recognition en Google Colab
!pip install face_recognition
from google.colab import files
import face_recognition

# Cargar imágenes
uploaded = files.upload()
uploaded = files.upload()

# Rest of your code
image_path_same_person_1 = 'carita1.jpg'
image_path_same_person_2 = 'carita2.jpg'
image_same_person_1 = face_recognition.load_image_file(image_path_same_person_1)
image_same_person_2 = face_recognition.load_image_file(image_path_same_person_2)

# Obtener características faciales
encoding_same_person_1 = face_recognition.face_encodings(image_same_person_1)[0]
encoding_same_person_2 = face_recognition.face_encodings(image_same_person_2)[0]

# Calcular la distancia
distance_same_person = face_recognition.face_distance([encoding_same_person_1], encoding_same_person_2)[0]

threshold = 0.6  # Umbral de distancia para determinar si son la misma persona
if distance_same_person < threshold:
    print("Las dos imágenes son de la misma persona.")
else:
    print("Las dos imágenes son de personas diferentes.")