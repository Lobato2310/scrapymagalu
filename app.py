import scrapy
import scrapy.responsetypes

class Magalu(scrapy.Spider):
    name= 'm'
    page = 1
    custom_settings = {
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }

    def start_requests(self):
        yield scrapy.Request(f'https://www.magazineluiza.com.br/ferramentas/l/fs/?page={self.page}')

    def parse(self, response):
        blocos = response.xpath('//div[@data-testid="product-list"]//li')
        for bloco in blocos:
            title = bloco.xpath('.//h2[@data-testid="product-title"]//text()').get
            price = bloco.xpath('.//p[@data-testid="price-value"]//text()').get
            yield {
                'title' : title,
                'price' : price
            }
            if response.xpath('//button[@type="next"]').get():
                self.page += 1
                yield scrapy.Request(f'https://www.magazineluiza.com.br/ferramentas/l/fs/?page={self.page}', callback=self.parse)
     