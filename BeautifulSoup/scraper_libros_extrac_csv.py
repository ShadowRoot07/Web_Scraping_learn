import requests
from bs4 import BeautifulSoup
import csv  # Importamos el módulo para CSV

url = "http://books.toscrape.com/"
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, 'html.parser')

libros = soup.find_all('article', class_='product_pod')

# --- CONFIGURACIÓN DEL ARCHIVO CSV ---
# 'w' es para escribir (write), newline='' evita líneas vacías extra
with open("mis_libros.csv", "w", newline='', encoding="utf-8") as archivo_csv:
    # Definimos los nombres de las columnas
    columnas = ['Titulo', 'Precio']
    escritor = csv.DictWriter(archivo_csv, fieldnames=columnas)
    
    # Escribimos el encabezado (la primera fila con los nombres)
    escritor.writeheader()

    for libro in libros:
        titulo = libro.h3.a.get('title')
        precio = libro.find('p', class_='price_color').text
        
        # Escribimos una fila con los datos recolectados
        escritor.writerow({'Titulo': titulo, 'Precio': precio})

print("¡Datos guardados con éxito en mis_libros.csv!")

