import scrapy
from scrapy_learn.items import NovelItem
import time


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['www.xbiquge.la/72/72098/']
    start_urls = ['http://www.xbiquge.la/72/72098/']  # 小说页地址，有章节列表的那种

    def start_requests(self):
        for url in self.start_urls:  # 将cookie交给scrapy
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84"
            }
            yield scrapy.Request(url=url, headers=headers, meta={"headers": headers}, dont_filter=True,
                                 callback=self.parse)

    def parse(self, response):
        chapter_url_list = response.css('#list dd a::attr(href)').extract()
        novel_item = NovelItem()
        novel_item['novel_title'] = response.css('#info h1::text').extract()    # 小说名

        # for url in chapter_url_list[0:2]: # 调试只获取2章
        for url in chapter_url_list:
            url = 'https://www.xbiquge.la' + url
            time.sleep(1)
            yield scrapy.Request(url=url, meta={"chapter_title_list": chapter_url_list, 'item': novel_item},
                                 dont_filter=True, callback=self.parse_page)

    def parse_page(self, response):
        novel_item = response.meta.get('item')
        novel_item['chapter_name'] = response.css('.bookname h1::text').extract()
        novel_item['chapter_content'] = response.css('#content::text').extract()

        yield novel_item
