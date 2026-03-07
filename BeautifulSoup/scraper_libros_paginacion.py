import requests
from bs4 import BeautifulSoup
import csv

url_base = "http://books.toscrape.com/catalogue/"
url_actual = "http://books.toscrape.com/catalogue/page-1.html"

# Preparamos el archivo CSV antes de empezar el bucle
with open("todos_los_libros.csv", "w", newline='', encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(['Titulo', 'Precio'])

    # Bucle infinito que se romperá cuando no haya más páginas
    while url_actual:
        print(f"Raspando: {url_actual}")
        res = requests.get(url_actual)
        soup = BeautifulSoup(res.text, 'html.parser')

        # --- Lógica de extracción (lo que ya sabes) ---
        libros = soup.find_all('article', class_='product_pod')
        for libro in libros:
            titulo = libro.h3.a.get('title')
            precio = libro.find('p', class_='price_color').text
            escritor.writerow([titulo, precio])

        # --- Lógica de Paginación ---
        # Buscamos el botón "Next"
        boton_next = soup.find('li', class_='next')
        
        if boton_next:
            # Extraemos el href (ej: 'page-2.html')
            ruta_siguiente = boton_next.a.get('href')
            # Construimos la URL completa para la siguiente vuelta
            url_actual = url_base + ruta_siguiente
        else:
            # Si no hay botón "Next", el bucle termina
            url_actual = None
            print("¡Hemos llegado al final!")

