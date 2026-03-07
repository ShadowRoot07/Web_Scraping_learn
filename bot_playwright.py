# bot_playwright.py
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Lanzamos el navegador (Chromium es el estándar)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("🌐 Navegando a la tienda de libros...")
        page.goto("http://books.toscrape.com/")
        
        # En Playwright, los selectores son más modernos
        titulo = page.title()
        print(f"✅ Título capturado: {titulo}")
        
        # Extraer el primer libro para probar
        primer_libro = page.locator(".product_pod h3 a").first.get_attribute("title")
        print(f"📖 Primer libro encontrado: {primer_libro}")
        
        browser.close()

if __name__ == "__main__":
    run()

