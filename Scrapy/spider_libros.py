import scrapy

class LibrosSpider(scrapy.Spider):
    # 1. El nombre de la araña (identificador único)
    name = "buscador_libros"

    # 2. Las URLs por donde empezará a navegar
    start_urls = ["http://books.toscrape.com/"]

    # 3. El método principal que procesa la respuesta de la web
    def parse(self, response):
        print("🔎 Analizando la página con Scrapy...")
        
        # Buscamos todos los artículos de libros
        for libro in response.css("article.product_pod"):
            # Usamos 'yield' para entregar los resultados como un diccionario
            yield {
                "titulo": libro.css("h3 a::attr(title)").get(),
                "precio": libro.css("p.price_color::text").get(),
                "disponibilidad": libro.css("p.instock.availability::text").getall()[-1].strip()
            }
        
        # Lógica de paginación (Opcional por ahora)
        siguiente_pagina = response.css("li.next a::attr(href)").get()
        if siguiente_pagina is not None:
            # Scrapy sigue el enlace automáticamente
            yield response.follow(siguiente_pagina, callback=self.parse)

