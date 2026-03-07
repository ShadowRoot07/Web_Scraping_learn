from requests_html import HTMLSession

# 1. Creamos la sesión especial
session = HTMLSession()

url = "https://example.com/pagina-con-javascript"

# 2. Hacemos la petición
r = session.get(url)

# 3. ¡MAGIA! Esto le dice a Python: "Ejecuta el JS y espera a que termine"
# scrolldown: simula bajar la página para cargar más contenido
# sleep: espera unos segundos para que todo aparezca
r.html.render(sleep=3, scrolldown=2)

# 4. Ahora ya podemos buscar elementos como antes
productos = r.html.find('.clase-dinamica')

for producto in productos:
    print(producto.text)

