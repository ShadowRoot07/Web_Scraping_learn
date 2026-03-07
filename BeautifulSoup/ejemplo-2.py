# Extraccion por etiquetas y clases
import requests
from bs4 import BeautifulSoup

# Simulamos una respuesta para el ejemplo
html_ejemplo = """
<div class="producto">
    <h2 class="nombre">Laptop Pro</h2>
    <span class="precio">$1200</span>
</div>
<div class="producto">
    <h2 class="nombre">Teclado Mecánico</h2>
    <span class="precio">$80</span>
</div>
"""

soup = BeautifulSoup(html_ejemplo, 'html.parser')

# 1. Extraer el nombre del primer producto
primer_nombre = soup.find('h2', class_='nombre').text
print(f"Producto: {primer_nombre}")

# 2. Extraer TODOS los precios
todos_los_precios = soup.find_all('span', class_='precio')

for precio in todos_los_precios:
    print(f"Precio encontrado: {precio.text}")

