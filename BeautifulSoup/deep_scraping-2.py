import requests
from bs4 import BeautifulSoup
import csv
import time # Para ser "caballerosos" con el servidor

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8"
}

url = "http://books.toscrape.com/"

# Ahora tus peticiones van "protegidas"
res = requests.get(url, headers=headers)
# ... el resto del código de BeautifulSoup sigue igual


url_base = "http://books.toscrape.com/"
url_catalogo = "http://books.toscrape.com/catalogue/"

# 1. Preparamos el archivo CSV
with open("detalles_libros.csv", "w", newline='', encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(['Titulo', 'Precio', 'Descripcion'])

    # 2. Petición a la página principal
    res_principal = requests.get(url_base)
    soup_principal = BeautifulSoup(res_principal.text, 'html.parser')
    libros = soup_principal.find_all('article', class_='product_pod')

    for libro in libros:
        # Extraemos datos básicos de la superficie
        titulo = libro.h3.a.get('title')
        precio = libro.find('p', class_='price_color').text
        
        # OBTENEMOS EL ENLACE PARA EL DEEP SCRAPING
        # Nota: El link puede variar si estás en la home o en catálogo
        link_relativo = libro.h3.a.get('href')
        url_detalle = url_base + link_relativo.replace('catalogue/', '')

        print(f"Extrayendo detalles de: {titulo}...")

        # 3. ENTRANDO AL DETALLE (Nivel 2 de profundidad)
        time.sleep(1) # Esperamos 1 segundo entre peticiones
        res_detalle = requests.get(url_detalle)
        soup_detalle = BeautifulSoup(res_detalle.text, 'html.parser')

        # Localizamos la descripción
        # Buscamos el ID específico y luego su hermano (el párrafo)
        desc_div = soup_detalle.find('div', id='product_description')
        
        # Verificamos que exista (algunos libros podrían no tener descripción)
        descripcion = desc_div.find_next_sibling('p').text if desc_div else "Sin descripción"

        # 4. Guardamos la fila completa con el dato profundo
        escritor.writerow([titulo, precio, descripcion])

print("\n¡Proceso de Deep Scraping finalizado con éxito!")

