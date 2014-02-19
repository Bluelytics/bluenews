from scrapy.spider import Spider
from scrapy.selector import Selector

from bluecrawler.items import NewsItem

class LaNacionSpider(Spider):
    name = "lanacion"
    allowed_domains = ["lanacion.com.ar"]
    start_urls = [
        "http://buscar.lanacion.com.ar/dolar?sort=-modified"
    ]

    def parse(self, response):
        sel = Selector(response)
        latest_news = sel.xpath('//ul[@class="acumuladosBuscador"]/li')
        items = []
        for news in latest_news:
            item = NewsItem()
            item['url'] = news.xpath('span/h2/a/@onclick').extract()[0].split("'")[1]
            item['title'] = news.xpath('span/h2/a/text()').extract()[0]
            item['content'] = news.xpath('p/text()').extract()[0]
            items.append(item)

        return items

        