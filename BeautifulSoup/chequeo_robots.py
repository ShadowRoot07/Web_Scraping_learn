import requests

def revisar_permisos(url_base):
    robots_url = f"{url_base}/robots.txt"
    try:
        print(f"🕵️ Analizando reglas en: {robots_url}")
        respuesta = requests.get(robots_url)
        
        if respuesta.status_code == 200:
            print("--- CONTENIDO DEL ROBOTS.TXT ---")
            print(respuesta.text)
            print("-------------------------------")
            
            # Busquemos si hay alguna prohibición específica
            if "Disallow: /" in respuesta.text:
                print("⚠️ ¡Cuidado! Esta web pide que no entres a ciertas rutas.")
            else:
                print("✅ Parece que el camino está despejado.")
        else:
            print("ℹ️ No se encontró robots.txt, procede con cautela.")
            
    except Exception as e:
        print(f"❌ Error al conectar: {e}")

# Probemos con la web de práctica
revisar_permisos("http://books.toscrape.com")

