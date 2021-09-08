# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import re
import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.loader import ItemLoader


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def date_convert(value):
    """时间处理"""
    match_re = re.match(".*?(\d+.*)", value)
    if match_re:
        return match_re.group(1)  # 获取创建时间
    else:
        return "1970-09-01"


class ArticleItemLoader(ItemLoader):
    """继承ItemLoader"""
    default_input_processor = MapCompose()
    default_output_processor = TakeFirst()


class JobBoleArticlespiderItem(scrapy.Item):
    title = scrapy.Field()
    created_date = scrapy.Field(
        input_processor=MapCompose(date_convert),
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field()
    comment_nums = scrapy.Field()
    fav_nums = scrapy.Field()
    tags = scrapy.Field(
        output_processor=Join(separator=',')
    )
    content = scrapy.Field()
