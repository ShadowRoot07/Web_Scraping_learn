import scrapy

class DetalleSpider(scrapy.Spider):
    name = "detalles"
    start_urls = ["http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"]

    def parse(self, response):
        # Usando XPath (otra forma poderosa de Scrapy)
        yield {
            'nombre': response.xpath('//h1/text()').get(),
            'categoria': response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get(),
            'stock': response.css('p.instock.availability::text').getall()[1].strip(),
            'descripcion': response.xpath('//article/p/text()').get()
        }

