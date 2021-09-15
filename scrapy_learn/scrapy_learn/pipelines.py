# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import codecs

class Save2TxtPipeline:
    """保存到txt"""

    def process_item(self, item, spider):
        novel_title = item.get('novel_title')[0]  # 获取小说名创建同名目录
        if os.path.exists(novel_title):
            pass
        else:
            os.mkdir(novel_title)

        chapter_name = item.get('chapter_name')  # 章节名
        chapter_content = item.get('chapter_content')  # 章节内容
        print(chapter_name)
        print(chapter_content)
        chapter_content = map(str.lstrip, chapter_content)   # 去掉列表中头部空白字符
        file = codecs.open(r"{}/{}.txt".format(novel_title, str(chapter_name[0])), 'w',
                           encoding="utf-8")  # 打开文件，增量内容
        file.writelines(chapter_content)  # 写入字符串列表
        file.close()  # 别忘了关闭
        return item
