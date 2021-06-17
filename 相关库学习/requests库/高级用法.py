import requests

# 创建一个会话对象
# s = requests.Session()
#
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
#
# r = s.get("https://httpbin.org/cookies")
#
# print(r.text)

# {
#   "cookies": {
#     "sessioncookie": "123456789"
#   }
# }

# 请求与响应对象

r = requests.get("https://www.baidu.com")

print(r.headers)

# {'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'keep-alive',
#         'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Thu, 17 Jun 2021 15:52:48 GMT',
#         'Last-Modified': 'Mon, 23 Jan 2017 13:23:55 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18',
#         'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}

print(r.request.headers)

# {'User-Agent': 'python-requests/2.25.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*',
#      'Connection': 'keep-alive'}
