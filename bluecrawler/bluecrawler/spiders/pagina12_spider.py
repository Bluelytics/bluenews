from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders.crawl import CrawlSpider, Rule

from bluecrawler.items import NewsItem

import re


def process_onclick(value):
    m = re.search("canonical\('(.+?)'", value)
    if m:
        return m.group(1)


class Pagina12Spider(CrawlSpider):
    name = "pagina12"
    allowed_domains = ["pagina12.com.ar"]
    start_urls = [
        "http://www.pagina12.com.ar/buscador/resultado.php?q=dolar"
    ]
    rules=(
    Rule(SgmlLinkExtractor(allow=(),
                           restrict_xpaths='//div[@class="r_ocurrencia"]/h3/a'),
         callback='parse_item'),
    )

    def parse_item(self, response):
        sel = Selector(response)

        item = NewsItem()
        item['url'] = response.url
        item['date'] = ''
        item['title'] = sel.css('div.nota > h2').xpath('text()').extract()[0]
        item['content'] = "\n".join(sel.xpath('//div[@id="cuerpo"]/p/text()').extract())

        return item

        