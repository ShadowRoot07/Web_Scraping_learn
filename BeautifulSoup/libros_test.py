import requests

# Supongamos que esta es la web que queremos investigar
base_url = "http://books.toscrape.com/"

# Una lista de rutas donde suelen esconderse los datos (JSON)
rutas_api_comunes = [
    "api/v1/books",
    "static/data/books.json",
    "ajax/books"
]

for ruta in rutas_api_comunes:
    url_prueba = base_url + ruta
    try:
        res = requests.get(url_prueba, timeout=5)
        if res.status_code == 200:
            print(f"¡ENCONTRADA! Posible API en: {url_prueba}")
        else:
            print(f"Intentando en {ruta}... (Nada aquí)")
    except:
        pass

