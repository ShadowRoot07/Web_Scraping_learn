from playwright.sync_api import sync_playwright

def explorar():
    # 1. El Contexto: Abrimos el "motor" del navegador
    with sync_playwright() as p:
        # launch() enciende el programa (Chromium)
        browser = p.chromium.launch(headless=True)
        
        # new_page() es como abrir una pestaña nueva
        page = browser.new_page()

        # goto() es la orden de navegar
        print("🚀 Viajando a la web...")
        page.goto("http://books.toscrape.com/")

        # --- LA SINTAXIS CLAVE ---

        # locator() es el "puntero". Aquí buscamos elementos.
        # .all() nos da una lista de todos los que coincidan
        libros = page.locator(".product_pod").all()
        print(f"📦 He detectado {len(libros)} contenedores de libros.")

        for i, libro in enumerate(libros[:3]): # Solo los primeros 3 para no saturar
            # inner_text() extrae lo que el usuario ve en pantalla
            # .locator() se puede encadenar (buscar dentro de otro buscador)
            titulo = libro.locator("h3 a").inner_text()
            precio = libro.locator(".price_color").inner_text()
            
            print(f"📖 Libro {i+1}: {titulo} - Costo: {precio}")

        # Cerrar para liberar memoria en la nube
        browser.close()

if __name__ == "__main__":
    explorar()

