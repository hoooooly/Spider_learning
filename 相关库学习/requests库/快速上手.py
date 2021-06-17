# 安装requests模块
# pip install requests

# 导入requests
import requests

# 目标url
url = "https://www.baidu.com"

# 向目标url发送请求
response = requests.get(url)

# 设置响应编码方式
response.encoding = "utf-8"

# 打印响应内容
print(response.text)

# 打印响应内容, 二进制格式
print(response.content)

