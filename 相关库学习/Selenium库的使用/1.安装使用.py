# conding: utf-8
# pip install selenium
# install webdriver

from selenium import webdriver

# 如果你没有把chromedriver添加到系统环境变量中，executable_path参数要附上chromedriver的绝对路径
driver = webdriver.Chrome(executable_path="D:/tools/chromedriver")


# 使用phantomjs无界面浏览器, selenium高版本不支持
# driver = webdriver.PhantomJS(executable_path="D:/tools/phantomjs")


# 向一个url发起请求
driver.get("https://www.baidu.com")



def parse_cookies(json_cookies):
    """将获取到的json格式的cookies提取"""
    cookie = ""
    for json_cookie in json_cookies:
        cookie = cookie + str(json_cookie['name']) + ":" + str(json_cookie['value']) + ";"
    return cookie

cookie = parse_cookies(driver.get_cookies()) 

print(cookie)


# 打印页面的标题
print(driver.title)

# 把网页保存为图片
driver.save_screenshot("baidu.png")

# 退出模拟浏览器
driver.quit()
