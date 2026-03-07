import requests
from bs4 import BeautifulSoup

url_home = "http://books.toscrape.com/"
res = requests.get(url_home)
soup = BeautifulSoup(res.text, 'html.parser')

# 1. Buscamos el primer libro
primer_libro = soup.find('article', class_='product_pod')

# 2. Obtenemos el link de su página de detalles
link_relativo = primer_libro.h3.a.get('href')
url_detalle = url_home + link_relativo

print(f"Entrando a: {url_detalle}...\n")

# 3. ¡Hacemos una nueva petición a esa página específica!
res_detalle = requests.get(url_detalle)
soup_detalle = BeautifulSoup(res_detalle.text, 'html.parser')

# 4. Ahora extraemos algo que SOLO está adentro, como la descripción
# En esta web, la descripción es un <p> que no tiene clase, pero está 
# después de un div con id='product_description'
descripcion = soup_detalle.find('div', id='product_description').find_next_sibling('p').text

print("Descripción del libro:")
print(descripcion)

