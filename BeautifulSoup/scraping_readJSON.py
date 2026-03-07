import requests

# Imagina que esta es la URL secreta que encontraste inspeccionando la red
url_api_oculta = "https://api.coindesk.com/v1/bpi/currentprice.json"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
}

res = requests.get(url_api_oculta, headers=headers)

# En lugar de usar BeautifulSoup, usamos .json()
datos = res.json()

# Navegamos por el diccionario como ya sabes hacer en Python
precio_usd = datos['bpi']['USD']['rate']
actualizacion = datos['time']['updated']

print(f"El precio del Bitcoin es: ${precio_usd}")
print(f"Última actualización: {actualizacion}")

