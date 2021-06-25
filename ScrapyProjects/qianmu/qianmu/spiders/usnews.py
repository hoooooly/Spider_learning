import scrapy


class UsnewsSpider(scrapy.Spider):
    name = 'usnews'
    allowed_domains = ['www.qianmu.org']
    start_urls = ['http://www.qianmu.org/']

    def parse(self, response):
        pass
