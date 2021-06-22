import time
from selenium import webdriver

url = "https://www.holychan.ltd/"

driver = webdriver.Chrome(executable_path="D:/tools/chromedriver")
driver.get(url)
time.sleep(1)

# 定义一个js语句，滑动到页面底部
js = "window.scrollTo(0, document.body.scrollHeight)"
# 执行js的方法
driver.execute_script(js)

time.sleep(2)
driver.quit()
