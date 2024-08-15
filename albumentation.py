import albumentations as A
import cv2
import os
import random
from datetime import datetime
import shutil

# Directorios

# Rutas
input_folder = '/home/ada-lovelace/ultralytics/real images/valid/images'
label_folder = '/home/ada-lovelace/ultralytics/real images/valid/labels'
output_folder = '/home/ada-lovelace/ultralytics/val'
output_label_folder = '/home/ada-lovelace/ultralytics/lab'


# Declarar el pipeline de aumento
transform = A.Compose([
    A.HueSaturationValue(hue_shift_limit=15, sat_shift_limit=-25, val_shift_limit=-10, p=1),
    #A.RandomBrightnessContrast(brightness_limit=(-0.2, 0.2), contrast_limit=(-0.2, 0.2), brightness_by_max=True, p=1),
    #A.ChannelShuffle(p=1),
])

# Función para copiar y renombrar etiquetas
def copy_and_rename_label(original_label_path, new_label_path):
    if os.path.exists(original_label_path):
        shutil.copy(original_label_path, new_label_path)
    else:
        print(f"No se encontró el archivo de etiqueta: {original_label_path}")

# Recorrer los archivos de la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Filtrar por tipos de imagen
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        # Verificar si la imagen fue leída correctamente
        if image is None:
            print(f"Error al leer la imagen {image_path}")
            continue

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Aplicar las transformaciones
        transformed_image = image

        for transform_fn in transform.transforms:
            if transform_fn.p >= random.random():
                transformed_image = transform_fn(image=transformed_image)["image"]

        # Convertir de vuelta a BGR para guardar usando OpenCV
        transformed_image_bgr = cv2.cvtColor(transformed_image, cv2.COLOR_RGB2BGR)

        # Crear un nombre único para cada imagen transformada
        base_filename = os.path.splitext(filename)[0]
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        output_filename = f"{base_filename}_aug_{timestamp}.jpg"
        output_path = os.path.join(output_folder, output_filename)

        # Guardar la imagen transformada
        cv2.imwrite(output_path, transformed_image_bgr)
        print(f"Imagen transformada guardada como {output_path}")

        # Manejar el archivo de etiqueta
        label_filename = base_filename + '.txt'
        original_label_path = os.path.join(label_folder, label_filename)
        new_label_filename = f"{base_filename}_aug_{timestamp}.txt"
        new_label_path = os.path.join(output_label_folder, new_label_filename)

        copy_and_rename_label(original_label_path, new_label_path)
        print(f"Archivo de etiqueta copiado y renombrado como {new_label_path}")
