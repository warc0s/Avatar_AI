#!/usr/bin/env python3
from PIL import Image
import os

def join_images():
    # Lista para almacenar los nombres de archivos encontrados
    filenames = []
    
    # Para cada número del 1 al 8, se busca primero el archivo .png, y si no existe se busca .jpg
    for i in range(1, 9):
        png_filename = f"{i}.png"
        jpg_filename = f"{i}.jpg"
        if os.path.exists(png_filename):
            filenames.append(png_filename)
        elif os.path.exists(jpg_filename):
            filenames.append(jpg_filename)
        else:
            raise FileNotFoundError(f"No se encontró la imagen {i} con extensión png ni jpg.")
    
    # Abrir las imágenes y almacenarlas en una lista
    images = [Image.open(fn) for fn in filenames]
    
    # Se asume que todas las imágenes tienen las mismas dimensiones
    width, height = images[0].size
    mode = images[0].mode  # Modo de color (RGB, RGBA, etc.)
    
    # Crear una imagen nueva con 4 columnas y 2 filas
    new_width  = 4 * width
    new_height = 2 * height
    new_image = Image.new(mode, (new_width, new_height))
    
    # Pegar las imágenes en la nueva imagen:
    # Primera fila: imágenes 1 a 4
    for i in range(4):
        new_image.paste(images[i], (i * width, 0))
    
    # Segunda fila: imágenes 5 a 8
    for i in range(4, 8):
        new_image.paste(images[i], ((i - 4) * width, height))
    
    # Guardar la imagen resultante
    new_image.save('joined_image.png')
    print("La imagen se ha guardado como 'joined_image.png'.")

if __name__ == '__main__':
    join_images()
