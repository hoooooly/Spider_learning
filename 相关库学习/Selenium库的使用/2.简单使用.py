import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:/tools/chromedriver")

driver.get("https://www.baidu.com")

# # # 在对话框输入python
# driver.find_element_by_id("kw").send_keys('python')

# # # 点击百度搜索
# driver.find_element_by_id("su").click()

# # time.sleep(6)
# # 保存搜索截图
# driver.save_screenshot("baidu_python.png")


# # 显示源码
# print(driver.page_source)

# 显示响应对应的url
print(driver.current_url)
# https://www.baidu.com/

# 显示标题
print(driver.title)
# 百度一下，你就知道

time.sleep(2)
driver.get('http://www.douban.com')
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.close()

driver.quit()