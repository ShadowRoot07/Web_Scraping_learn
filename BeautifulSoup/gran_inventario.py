import requests
from bs4 import BeautifulSoup
import time

def scrap_agro_multi_paginas():
    gran_inventario = []
    # Simulamos que hay 3 páginas
    for pagina in range(1, 4):
        print(f"--- Raspando Página {pagina} ---")
        # Nota: Usamos una URL de prueba o la de los libros
        url = f"http://books.toscrape.com/catalogue/page-{pagina}.html"
        
        try:
            res = requests.get(url, timeout=10)
            soup = BeautifulSoup(res.text, 'html.parser')
            productos = soup.find_all('article', class_='product_pod')

            for p in productos:
                # Extraemos y limpiamos en un solo paso
                item = {
                    "nombre": p.h3.a.get('title').strip().capitalize(),
                    "precio": float(p.find('p', class_='price_color').text.replace('£', '')),
                    "origen_pag": pagina
                }
                gran_inventario.append(item)
            
            time.sleep(1) # Pausa de cortesía

        except Exception as e:
            print(f"Error en página {pagina}: {e}")

    return gran_inventario

# Ejecutamos
datos_finales = scrap_agro_multi_paginas()
print(f"\n¡Total de productos recolectados: {len(datos_finales)}!")

