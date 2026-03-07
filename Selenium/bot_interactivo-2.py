from selenium import webdriver
from selenium.webdriver.chrome.service import Service # <--- Esto es clave
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 1. LE DECIMOS DONDE ESTÁ EL DRIVER REALMENTE
# En Termux, chromedriver suele estar en esta ruta:
ruta_driver = "/data/data/com.termux/files/usr/bin/chromedriver"
servicio = Service(executable_path=ruta_driver)

try:
    # ... (el código de inicio que ya tienes) ...
    driver = webdriver.Chrome(service=servicio, options=options)
    driver.get("http://books.toscrape.com/")
    time.sleep(3)

    # 1. BUSCAR LA CATEGORÍA
    # Usaremos LINK_TEXT, que busca el texto exacto que ves en pantalla
    print("🎯 Buscando la sección 'Music'...")
    boton_musica = driver.find_element(By.LINK_TEXT, "Music")

    # 2. ACCIÓN: HACER CLIC
    print("🖱️ Haciendo clic...")
    boton_musica.click()

    # 3. ESPERAR A QUE CARGUE LA NUEVA PÁGINA
    time.sleep(3)
    print(f"📍 Ahora estamos en: {driver.title}")

    # 4. CONTAR ELEMENTOS
    # Cada libro está dentro de una etiqueta <article> con la clase 'product_pod'
    libros = driver.find_elements(By.CLASS_NAME, "product_pod")
    print(f"🎶 He encontrado {len(libros)} libros de música.")

    print("📋 Extrayendo detalles de los libros...")

    for libro in libros:
        # Dentro de cada 'libro', buscamos el título y el precio
        # Usamos CSS Selectors como aprendimos ayer
        titulo = libro.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        precio = libro.find_element(By.CSS_SELECTOR, "p.price_color").text
        
        print(f"📖 {titulo} | 💰 {precio}")

finally:
    driver.quit()

