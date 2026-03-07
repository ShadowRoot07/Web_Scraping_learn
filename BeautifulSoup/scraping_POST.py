import requests

url = "https://httpbin.org/post"

# 1. Los datos que queremos enviar al formulario
mis_datos = {
    "usuario": "ShadowRoot07",
    "tema": "Web Scraping",
    "mensaje": "Aprendiendo con mi IA favorita"
}

# 2. Enviamos la petición usando POST en lugar de GET
respuesta = requests.post(url, data=mis_datos)

# 3. Revisamos qué recibió el servidor
if respuesta.status_code == 200:
    print("¡Datos enviados con éxito!")
    # Mostramos la respuesta en formato JSON (un diccionario de Python)
    print(respuesta.json()['form']) 

