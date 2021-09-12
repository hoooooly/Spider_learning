# Scrapy settings for ArticleSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os
import sys

BOT_NAME = 'ArticleSpider'

SPIDER_MODULES = ['ArticleSpider.spiders']
NEWSPIDER_MODULE = 'ArticleSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ArticleSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 遵守robots协议，默认True，遵守。修改为False，不遵守
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ArticleSpider.middlewares.ArticlespiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# 下载中间件
DOWNLOADER_MIDDLEWARES = {
    # 'ArticleSpider.middlewares.RandomUserAgentMiddlware': 534,    # 设置代理user-agent
    # 'ArticleSpider.middlewares.ArticlespiderDownloaderMiddleware': None,
}

USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"

# 定义随机agent类型
RANDOM_UA_TYPE = "random"
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 配置item管道，默认不开启，
# 'ArticleSpider.pipelines.ArticlespiderPipeline': 300,300代表优先级，数字越小优先级越高
ITEM_PIPELINES = {
    'ArticleSpider.pipelines.ArticleImagePipeline': 1,  # 下载图片使用重写的ImagePipeline
    'ArticleSpider.pipelines.JosnWithEncodingPipeline': 2,  # 自定义保存文章到Json的pipeline
    'ArticleSpider.pipelines.JsonExporterPipeline': 3,  # 使用内置的Jsonexport导出json
    'ArticleSpider.pipelines.MysqlTwistedPipeline': 4,  # 异步实现写入MySQL数据库
    # 'ArticleSpider.pipelines.MysqlPipeline': 4,  # 把数据存入MySQL
    'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
}

"""安装图片处理库pip install pillow -i http://pypi.douban.com/simple"""
project_dir = os.path.dirname(os.path.abspath(__file__))  # 获取项目路径
IMAGES_STORE = os.path.join(project_dir, "images")  # 设置图片保存路径
IMAGES_URLS_FIELD = 'front_image_url'  # 图片的下载地址
# IMAGES_RESULT_FIELD = 'field_name_for_your_processed_images'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 定义数据库连接参数
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3307
MYSQL_DBNAME = "artice_spider"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"

# 知乎登录信息
USER = "17607119016"
PASSWORD = "Holy_zhihu_1314520"
