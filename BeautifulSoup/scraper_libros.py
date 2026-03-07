import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# 1. Buscamos TODOS los artículos que tengan la clase 'product_pod'
# Cada uno de estos es un libro individual
libros = soup.find_all('article', class_='product_pod')

print(f"He encontrado {len(libros)} libros.\n")

for libro in libros:
    # 2. Dentro de CADA libro, buscamos el título
    # El título suele estar dentro de un h3 -> a
    titulo = libro.h3.a.get('title') 
    
    # 3. Buscamos el precio usando su clase específica
    precio = libro.find('p', class_='price_color').text
    
    print(f"Libro: {titulo}")
    print(f"Precio: {precio}")
    print("-" * 20)

