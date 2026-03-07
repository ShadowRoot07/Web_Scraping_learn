import requests
from bs4 import BeautifulSoup

url_base = "http://books.toscrape.com/"
res = requests.get(url_base)
soup = BeautifulSoup(res.text, 'html.parser')

libros = soup.find_all('article', class_='product_pod')

for libro in libros:
    titulo = libro.h3.a.get('title')
    
    # 1. Buscamos la etiqueta <img> dentro del libro
    imagen_tag = libro.find('img')
    
    # 2. Extraemos el valor del atributo 'src'
    ruta_relativa = imagen_tag.get('src')
    
    # 3. Limpiamos y unimos la ruta para que sea un link real
    # En esta web las rutas vienen con '../../', las limpiamos un poco
    ruta_limpia = ruta_relativa.replace('../', '')
    url_completa_imagen = url_base + ruta_limpia
    
    print(f"Libro: {titulo}")
    print(f"URL Imagen: {url_completa_imagen}")
    print("-" * 30)

