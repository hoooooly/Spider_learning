import requests
import time
from lxml import etree
from selenium import webdriver

# 要请求的URL
url = "https://www.zhipin.com/c101280600/?query=%E7%88%AC%E8%99%AB&page=1&ka=page-1"

# 使用selenium模拟登录,获取cookie
def get_cookie(url):
    # 如果你没有把chromedriver添加到系统环境变量中，executable_path参数要附上chromedriver的绝对路径
    driver = webdriver.Chrome(executable_path="D:/tools/chromedriver")
    # 向一个url发起请求
    driver.get(url)
    json_cookies = driver.get_cookies()
    # 关闭模拟器
    driver.quit()
    cookie = ""
    for json_cookie in json_cookies:
        cookie = cookie + str(json_cookie['name']) + ":" + str(json_cookie['value']) + ";"
    return cookie
    

# 定义headers
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",
    "referer": url,
    "cookie": get_cookie(url=url),
}

# print(headers)
# 请求URL
# for i in range(10):
#     url = f"hhttps://www.zhipin.com/c101280600/?query=%E7%88%AC%E8%99%AB&page={i+1}&ka=page-{i+1}"
#     print(url)
# 定义headers
#     time.sleep(1)

r = requests.get(url=url, headers=headers)
print(r.text)
# tree = etree.HTML(r.text)
# job_name_list =  tree.xpath('//div[@class="job-title"]//a/@href')
# print(job_name_list)
# for job in job_name_list:
#     print(job.strip())

# //span[@class="job-name"]/a/text()


# with open("python.html", "a+") as f:
#     f.write(r.content)
