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


class LaNacionSpider(CrawlSpider):
    name = "lanacion"
    allowed_domains = ["lanacion.com.ar"]
    start_urls = [
        "http://buscar.lanacion.com.ar/dolar?sort=-modified"
    ]
    rules=(
    Rule(SgmlLinkExtractor(allow=(),
                           attrs=('onclick',),
                           restrict_xpaths='//ul[@class="acumuladosBuscador"]/li/span/h2/a',
                           process_value=process_onclick),
         callback='parse_item'),
    )

    def parse_item(self, response):
        sel = Selector(response)

        item = NewsItem()
        item['url'] = response.url
        item['date'] = sel.xpath('//span[@itemprop="datePublished"]/text()').extract()[0]
        item['title'] = sel.xpath('//h1[@itemprop="name"]/text()').extract()[0]
        item['content'] = "\n".join(sel.xpath('//section[@itemprop="articleBody"]/p/text()').extract())

        return item

        