import time
from selenium import webdriver

url = "https://www.baidu.com"

driver = webdriver.Chrome(executable_path="D:/tools/chromedriver")

# 设置位置之后的所有元素定位操作都有最大等待时间十秒，在10秒内会定期进行元素定位，超出设置时间后将会报错
driver.implicitly_wait(10)

driver.get(url)

el = driver.find_element_by_xpath('//*[@id="lg"]/img[10000]')
print(el)

driver.quit()
