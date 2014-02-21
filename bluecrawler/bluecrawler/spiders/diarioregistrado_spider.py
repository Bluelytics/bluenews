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


class DiarioRegistradoSpider(CrawlSpider):
    name = "diarioregistrado"
    allowed_domains = ["diarioregistrado.com"]
    start_urls = [
        "http://www.diarioregistrado.com/news/search?q=dolar"
    ]
    rules=(
    Rule(SgmlLinkExtractor(allow=(),
                           restrict_xpaths='//div[@class="formato1 brd_b imagen"]/div[@class="texto"]/div/h2/a'),
         callback='parse_item'),
    )

    def parse_item(self, response):
        sel = Selector(response)

        item = NewsItem()
        item['url'] = response.url
        item['date'] = ''
        item['title'] = sel.xpath('//div[@id="cabecera_nota"]/h1/text()').extract()[0]
        item['content'] = "\n".join(sel.xpath('//div[@id="cuerpo_nota"]/p/text()').extract())

        return item

        