import re
import json
import scrapy
import requests
from urllib import parse
from scrapy import Request
# from scrapy.loader import ItemLoader
from ArticleSpider.utils import zhihu_login
from ArticleSpider.settings import USER, PASSWORD

"""scrapy 是异步IO框架，没有多线程，没有引入消息队列"""


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com/']
    start_urls = ['https://www.zhihu.com/']
    custom_settings = {
        "COOKIES_ENABLED": True
    }

    def start_requests(self):
        """
            在这里模拟登录拿到cookies
            两种滑动验证码方案：
            1.使用OpenCV识别
            2.使用机器学习方法识别
        """
        login = zhihu_login.Login(USER, PASSWORD, 2)
        cookie_dict = login.login()
        for url in self.start_urls:
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84"
            }
            yield scrapy.Request(url=url, headers=headers, cookies=cookie_dict,
                                 dont_filter=True, callback=self.parse_detail)

    def parse_detail(self, response):
        pass