#!/usr/bin/env python3

import os
import random
import string
import time
import shutil  # Para borrar carpetas y su contenido

def generate_random_string(length=100):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_edit_delete_file():
    folder_name = "DONT DELETE THIS FOLDER"
    
    # Crear o asegurar que existe la carpeta
    os.makedirs(folder_name, exist_ok=True)

    while True:
        try:
            # Crear un archivo con nombre aleatorio dentro de la carpeta
            file_name = os.path.join(folder_name, f"{generate_random_string(8)}.txt")

            # Escribir contenido aleatorio
            with open(file_name, "w") as file:
                for _ in range(random.randint(10, 100)):
                    file.write(generate_random_string(100) + "\n")
            print(f"Created: {file_name}")

            time.sleep(2)

            # Sobrescribir con nuevo contenido aleatorio
            with open(file_name, "w") as file:
                for _ in range(random.randint(10, 100)):
                    file.write(generate_random_string(100) + "\n")
            print(f"Edited: {file_name}")

            time.sleep(1)

            # Cada cierto tiempo, eliminar TODO el contenido de la carpeta
            if random.random() < 0.4:  # 40% de probabilidad de limpiar tras cada edición
                shutil.rmtree(folder_name)
                os.makedirs(folder_name, exist_ok=True)
                print(f"All contents of '{folder_name}' have been deleted.")

            time.sleep(1)

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(5)

if __name__ == "__main__":
    create_edit_delete_file()
