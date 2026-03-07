# Ectraccion Basica de datos de una pagina
import requests
from bs4 import BeautifulSoup

# 1. Definimos la URL
url = "https://www.google.com" 

# 2. Realizamos la petición
respuesta = requests.get(url)

# 3. Verificamos si la conexión fue exitosa (Status 200)
if respuesta.status_code == 200:
    print("¡Conexión exitosa!")
    
    # 4. Convertimos el contenido en un objeto de BeautifulSoup
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    
    # 5. Imprimimos el título de la página para probar
    print(f"Título de la web: {soup.title.string}")
else:
    print(f"Error al conectar: {respuesta.status_code}")

