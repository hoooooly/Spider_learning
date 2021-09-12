# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import codecs
import json
import time

import MySQLdb
import MySQLdb.cursors
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline  # 引入内置的ImagesPipeline
from scrapy.exporters import JsonItemExporter  # 引入内置的JsonItemExporter
from twisted.enterprise import adbapi


class ArticlespiderPipeline:
    def process_item(self, item, spider):
        return item


class MysqlPipeline():
    """
    把数据存入MySQL，同步方法，不建议采用
    安装MySQL驱动： pip install mysqlclient -i http://pypi.douban.com/simple
    """

    def __init__(self):
        self.conn = MySQLdb.connect(host="127.0.0.1", port=3307, user="root", passwd="root", database="artice_spider",
                                    charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into jobble_artice(title, url, url_object_id, front_image_url, front_image_path, praise_nums, comment_nums, fav_nums, tags, content, created_date) 
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        params = list()
        params.append(item.get("title", ""))  # title
        params.append(item.get("url",
                               ""))  # urlparams = {list: 11} ['微软将阻止Outlook 2010和更早版本连接到Microsoft 365 Exchange服务器', 'https://news.cnblogs.com/n/701633/', '41ee656920b66da1e5680298d00e04c2', 'https://images0.cnblogs.com/news_topic/20150604112810426.png', '', 0, 0, 1, 'Outlook', '<div id="news_content">\n            <… View
        params.append(item.get("url_object_id", ""))  # url_object_id
        front_image_url = "".join(item.get("front_image_url", []))
        params.append(front_image_url)  # front_image_url
        params.append(item.get("front_image_path", ""))  # front_image_path
        params.append(item.get("praise_nums", 0))  # praise_nums
        params.append(item.get("comment_nums", 0))  # comment_nums
        params.append(item.get("fav_nums", 0))  # fav_nums
        params.append(item.get("tags", ""))  # tags
        params.append(item.get("content", ""))  # content
        params.append(item.get("created_date", "1970-07-01"))  # created_date

        self.cursor.execute(insert_sql, params)  # 执行sql语句
        self.conn.commit()  # 提交
        return item

    def spider_closed(self):
        self.conn.close()


class MysqlTwistedPipeline(object):
    """异步实现写入MySQL数据库"""

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            port=settings["MYSQL_PORT"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)

    def handle_error(self, failure, item, spider):
        print(failure)

    def do_insert(self, cursor, item):
        insert_sql = """
                    insert into jobble_artice(title, url, url_object_id, front_image_url, front_image_path, praise_nums, comment_nums, fav_nums, tags, content, created_date)
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) on duplicate key update praise_nums = values(praise_nums)
                """

        params = list()
        params.append(item.get("title", ""))  # title
        params.append(item.get("url", ""))
        params.append(item.get("url_object_id", ""))  # url_object_id
        front_image_url = "".join(item.get("front_image_url", []))
        params.append(front_image_url)  # front_image_url
        params.append(item.get("front_image_path", ""))  # front_image_path
        params.append(item.get("praise_nums", 0))  # praise_nums
        params.append(item.get("comment_nums", 0))  # comment_nums
        params.append(item.get("fav_nums", 0))  # fav_nums
        params.append(item.get("tags", ""))  # tags
        params.append(item.get("content", ""))  # content
        params.append(item.get("created_date", "1970-07-01"))  # created_date
        cursor.execute(insert_sql, params)


class JosnWithEncodingPipeline(object):
    """自定义json文件的导出"""

    def __init__(self):
        self.file = codecs.open("article.json", "a", encoding="utf-8")  # 打开文件，增量添加内容

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"  # 编码json文件
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()  # 关闭文件


class JsonExporterPipeline(object):
    """使用内置的Jsonexport导出json"""

    def __init__(self):
        self.file = codecs.open("article_json_export.json", "wb")  # 打开文件,以二进制方式
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)  # 实列化导出器
        self.exporter.start_exporting()  # 初始化启动导出

    def process_item(self, item, spider):
        self.exporter.export_item(item)  # 传入item导出
        return item

    def spider_closed(self, spider):
        self.exporter.finish_exporting()  # 关闭导出器
        self.file.close()  # 关闭文件


class ArticleImagePipeline(ImagesPipeline):
    """自定义的图片下载管道，继承自ImagesPipeline"""

    def item_completed(self, results, item, info):
        """重写ImagesPipeline中的item_completed方法,将图片的保存路径放到JobBoleArticlespiderItem中"""
        if "front_image_url" in item:
            for ok, value in results:
                image_file_path = value['path']
                item["front_image_path"] = image_file_path
        return item
