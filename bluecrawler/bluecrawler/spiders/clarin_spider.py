from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders.crawl import CrawlSpider, Rule

from bluecrawler.items import NewsItem

import re



class ClarinSpider(CrawlSpider):
    name = "clarin"
    allowed_domains = ["clarin.com"]
    start_urls = [
        "http://buscador.clarin.com/dolar?order=0and;filter=content_section:Econom%C3%ADa;content_type:NWS;and;"
    ]
    rules=(
    Rule(SgmlLinkExtractor(allow=(),
                           restrict_xpaths='//ul[@class="desc"]/li[@class="txt"]/h2/a'),
         callback='parse_item'),
    )

    def parse_item(self, response):
        sel = Selector(response)
        
        item = NewsItem()
        item['url'] = response.url
        item['date'] = " ".join(sel.xpath('//div[@class="dia-hora"]/text()').extract() + sel.xpath('//div[@class="dia-hora"]/span/text()').extract())
        item['title'] = sel.xpath('//div[@class="resize"]/h2/text()').extract()[0]
        item['content'] = "\n".join(sel.xpath('//div[@class="bb-tu first-t interior"]/p/text()').extract())
        return item

        