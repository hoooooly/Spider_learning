import re
import json
import scrapy
import requests
from scrapy import Request
# from scrapy.loader import ItemLoader
from urllib import parse  # python3环境
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
            1.使用OpenCV识别，识别率相对较低
            2.使用机器学习方法识别, 可以使用百度大脑训练物体识别模型
        """
        login = zhihu_login.Login(USER, PASSWORD, 2)
        cookie_dict = login.login()

        for url in self.start_urls:
            headers = {
                "HOST": "www.zhihu.com",
                "Referer": "https://www.zhizhu.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
            }
            yield scrapy.Request(url=url, headers=headers, cookies=cookie_dict,
                                 dont_filter=True, callback=self.parse)

    def parse(self, response):
        """
        提取HTML页面中的所有url,并跟踪这些URL进行下一步爬取
        如果提取的URL的格式为/questuion/xxxx 就下载之后直接进入解析函数
        :param response:
        :return:
        """
        all_urls = response.css("a::attr(href)").extract()
        all_urls = [parse.urljoin(response.url, url) for url in all_urls]
        print(all_urls)

    def parse_detail(self, response):
        pass
