# PlayWright/extractor_imagenes.py
from playwright.sync_api import sync_playwright
import os

def capturar_portada():
    with sync_playwright() as p:
        # 1. Iniciamos el navegador
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("🚀 Conectando a la tienda para extraer imágenes...")
        page.goto("http://books.toscrape.com/")

        # 2. Localizamos la primera imagen de un libro
        # Usamos un selector CSS que llega hasta la etiqueta <img>
        selector_imagen = ".product_pod img"
        primer_libro_img = page.locator(selector_imagen).first
        
        # 3. Obtenemos la URL de la imagen (el atributo 'src')
        # Las URLs suelen ser relativas, así que Playwright nos ayuda a verlas
        url_relativa = primer_libro_img.get_attribute("src")
        url_completa = f"http://books.toscrape.com/{url_relativa}".replace("../", "")
        
        print(f"📸 URL de la imagen encontrada: {url_completa}")

        # 4. Definimos la ruta de guardado
        # Usamos tu carpeta 'archivos_extraidos'
        ruta_guardado = "archivos_extraidos/portada_libro.jpg"
        
        # 5. Descargamos la imagen usando una petición dentro del navegador
        respuesta = page.request.get(url_completa)
        
        # Creamos el archivo físico
        with open(ruta_guardado, "wb") as f:
            f.write(respuesta.body())
            
        print(f"✅ Imagen guardada con éxito en: {ruta_guardado}")

        browser.close()

if __name__ == "__main__":
    capturar_portada()

