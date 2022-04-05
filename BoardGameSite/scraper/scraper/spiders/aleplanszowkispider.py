import scrapy
from ..items import AlePlanszowkiGameItem
from BoardGameSiteApp.models import AlePlanszowkiGame

class AlePlanszowkiSpider(scrapy.Spider):
    name = 'aleplanszowki'
    start_urls = ["https://aleplanszowki.pl/368-gry-planszowe-i-towarzyskie"]

    def parse(self, response, **kwargs):
        for game in response.css('div.product-container'):
            item = AlePlanszowkiGame()
            item['name'] = game.css('a.product-name::text').get()
            item['price'] = game.css('span.price::text').get().replace('zł', '').replace(",", ".").replace(" ","")
            item['link'] = game.css('a.product-name').attrib['href']
            try:
                out_of_stock = game.css('span.out-of-stock')
                availability = False
            except Exception:
                availability = True
            item['availability'] = availability
            yield item

        next_page = response.css('li.pagination_next').css('a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)