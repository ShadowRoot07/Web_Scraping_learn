import requests

url = "http://books.toscrape.com/"

# Definimos nuestra "identidad falsa"
# Este es un User-Agent real de un navegador Chrome en Windows
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Enviamos la petición incluyendo los headers
respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
    print("¡El servidor nos dejó pasar pensando que somos un humano!")

