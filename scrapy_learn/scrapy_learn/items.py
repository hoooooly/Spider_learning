# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyLearnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NovelItem(scrapy.Item):
    """
    小说名
    章节名
    章节内容
    """
    novel_title = scrapy.Field()
    chapter_name = scrapy.Field()
    chapter_content = scrapy.Field()
