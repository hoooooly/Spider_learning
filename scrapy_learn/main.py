from scrapy.cmdline import execute

import sys
import os

# 添加当前目录到系统路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 启动scrapy，便于调试
execute(["scrapy", "crawl", "biquge"])
