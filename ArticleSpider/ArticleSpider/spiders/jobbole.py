import re
import json
import scrapy
import requests
from urllib import parse
from scrapy import Request
# from scrapy.loader import ItemLoader
from ArticleSpider.items import JobBoleArticlespiderItem, ArticleItemLoader
from ArticleSpider.utils import common

"""scrapy 是异步IO框架，没有多线程，没有引入消息队列"""


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['http://news.cnblogs.com/']
    custom_settings = {
        "COOKIES_ENABLED": True
    }

    def start_requests(self):
        """入口模拟登录那倒cookie，特殊网站使用不被识别的selenium
        pipenv install undetected-chromedriver -i https://pypi.douban.com/simple
        pipenv install selenium -i https://pypi.douban.com/simple
        :return:
        """
        import undetected_chromedriver.v2 as uc
        chrome = uc.Chrome()  # 实例化一个浏览器对象
        chrome.get('https://account.cnblogs.com/signin')
        # 自动化输入，自动化识别滑动验证码并拖动整个自动化验证过程
        input("请输入密码并登录页面，回车继续：")
        cookies = chrome.get_cookies()
        cookie_dict = {}  # 创建一个cookie字典,存入获取到的cookie值
        for cookie in cookies:
            cookie_dict[cookie['name']] = cookie['value']
            print(cookie_dict)

        for url in self.start_urls:
            # 将cookie交给scrapy
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84"
            }
            yield scrapy.Request(url=url, headers=headers, cookies=cookie_dict,
                                 dont_filter=True)

    def parse(self, response):
        """
        1.获取新闻列表页中的新闻URL并交给scrapy下载并调用相对应的解析方法
        2.获取下一页的url并交给scrapy进行下载，下载完成后交给parse继续跟进
        # """
        post_nodes = response.css('#news_list .news_block')
        # post_nodes = response.css('#news_list .news_block')[:1]  # debug
        for post_node in post_nodes:
            image_url = post_node.css('.entry_summary a img::attr(src)').extract_first("")
            if image_url.startswith("//"):
                image_url = "https:" + image_url
            post_url = post_node.css('h2 a::attr(href)').extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url},
                          callback=self.parse_detail)  # meta用于参数传递

        # 提取下一页并交给scrapy下载
        # next = response.css('div.pager a:last-child::text').extract_first("")  # 使用css
        next_ = response.xpath('//a[contains(text(), "Next >")]/@href').extract_first("")  # 使用Xpath
        if next_ == "Next >":
            next_url = response.css('div.pager a:last-child::attr(href)').extract_first("")
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)  # 继续交给self.parse解析下一个页面

    def parse_detail(self, response):
        """
        文章详情页的解析
        pip install requests -i https://pypi.douban.com/simple
        :param response:
        :return:
        """
        match_re = re.match(".*?(\d+)", response.url)
        if match_re:
            content_id = match_re.group(1)  # 获取文章号，交给scrapy发起请求获取浏览、评论、点赞数
            # title = response.css('#news_title a::text').extract_first("")  # 文章标题
            # created_date = response.css("#news_info .time::text").extract_first("")  # 创建时间
            # content = response.css("#news_content").extract()[0]  # 文章详情，html
            # tag_list = response.css(".news_tags a::text").extract()  # 获取标签list
            #
            # # title = response.xpath("//*[@id='news_title']//a/text()")
            # # create_date = response.xpath("//*[@id='news_info']//*[@class='time']/text()")
            # # content = response.xpath("//*[@id='news_content']").extract()[0]
            # #  tag_list = response.xpath("//*[@class='news_content']//a/text()").extract()
            #
            # tags = ','.join(tag_list)  # 标签
            #
            # match_re = re.match(".*?(\d+.*)", create_date)
            # if match_re:
            #     create_date = match_re.group(1)  # 获取创建时间
            #
            # artice_item = JobBoleArticlespiderItem()  # 定义文章item
            # artice_item["title"] = title
            # artice_item["created_date"] = created_date
            # artice_item["content"] = content
            # artice_item["tags"] = tags
            # artice_item["url"] = response.url
            # if response.meta.get("front_image_url", ""):
            #     artice_item["front_image_url"] = [
            #         response.meta.get("front_image_url", "")]  # 这里必须传入list，scrapy会遍历这个地址下载图片
            # else:
            #     artice_item["front_image_url"] = []  # 这里必须传入list可以为空但不能为空字符串

            item_loader = ArticleItemLoader(item=JobBoleArticlespiderItem(), response=response)
            item_loader.add_css("title", "#news_title a::text")
            item_loader.add_css("created_date", "#news_info .time::text")
            item_loader.add_css("content", "#news_content")
            item_loader.add_css("tags", ".news_tags a::text")
            item_loader.add_value("url", response.url)
            if response.meta.get("front_image_url", []):
                print([response.meta.get("front_image_url", "")])
                item_loader.add_value("front_image_url", [response.meta.get("front_image_url", "")])

            # artice_item = item_loader.load_item()

            """在scrapy中不建议使用requests同步框架"""
            yield Request(url=parse.urljoin(response.url, "/NewsAjax/GetAjaxNewsInfo?contentId={}".format(content_id)),
                          meta={"item_loader": item_loader, "url": response.url}, callback=self.parse_nums)

    def parse_nums(self, response):
        j_data = json.loads(response.text)
        item_loader = response.meta.get("item_loader", "")

        praise_nums = j_data["DiggCount"]  # 支持数
        fav_nums = j_data["TotalView"]  # 浏览数
        comment_nums = j_data["CommentCount"]  # 评论数

        item_loader.add_value("praise_nums", praise_nums)
        item_loader.add_value("fav_nums", fav_nums)
        item_loader.add_value("comment_nums", comment_nums)
        item_loader.add_value("url_object_id", common.get_md5(response.meta.get("url", "")))

        # artice_item = response.meta.get("artice_item", "")  # 拿到从parse_detail中传递过来的artice_item对象
        # artice_item["praise_nums"] = praise_nums
        # artice_item["fav_nums"] = fav_nums
        # artice_item["comment_nums"] = comment_nums
        # artice_item["url_object_id"] = common.get_md5(artice_item["url"])

        article_item = item_loader.load_item()
        article_item["front_image_url"] = [article_item["front_image_url"]]

        yield article_item  # 抛出artice_item给piplines处理
