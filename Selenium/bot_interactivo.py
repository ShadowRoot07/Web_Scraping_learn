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

# 2. INICIAMOS CON EL SERVICIO MANUAL
try:
    print("🚀 Iniciando motor manual para Termux...")
    driver = webdriver.Chrome(service=servicio, options=options)
    
    # ... (El resto de tu código de ayer igual) ...
    driver.get("http://books.toscrape.com/")

    # 1. Le damos 3 segundos para que cargue el título y el HTML
    print("⏳ Esperando a que la página despierte...")
    time.sleep(3)

    print(f"✅ ¡Conectado! Título: {driver.title}")

finally:
    if 'driver' in locals():
        driver.quit()

