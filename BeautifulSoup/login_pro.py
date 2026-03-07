import requests
from bs4 import BeautifulSoup

# URLs del sitio
url_login = "http://quotes.toscrape.com/login"

# 1. Configuramos Headers para parecer un navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Iniciamos una "Sesión". Esto es clave para que Python mantenga 
# las cookies del login en las siguientes peticiones.
sesion = requests.Session()

# --- PASO 1: OBTENER EL TOKEN ---
print("Obteniendo el token de seguridad...")
res_get = sesion.get(url_login, headers=headers)
soup_login = BeautifulSoup(res_get.text, 'html.parser')

# Buscamos el input que tiene el nombre 'csrf_token'
# <input type="hidden" name="csrf_token" value="abc123token...">
token = soup_login.find('input', attrs={'name': 'csrf_token'}).get('value')

print(f"¡Token robado con éxito!: {token[:15]}...")

# --- PASO 2: ENVIAR EL FORMULARIO ---
# Los nombres de los campos (username, password) se sacan mirando el HTML
datos_login = {
    "csrf_token": token,
    "username": "ShadowRoot07",
    "password": "password123" # En esta web puedes poner cualquier cosa
}

print("Intentando iniciar sesión...")
res_post = sesion.post(url_login, data=datos_login, headers=headers)

# --- PASO 3: VERIFICAR ---
soup_home = BeautifulSoup(res_post.text, 'html.parser')
boton_logout = soup_home.find('a', href='/logout')

if boton_logout:
    print("\n¡ÉXITO! Estamos dentro del sistema.")
    print("Ahora podríamos extraer datos que solo ven los usuarios registrados.")
else:
    print("\nFallo en el login. El token no funcionó o los datos son incorrectos.")

