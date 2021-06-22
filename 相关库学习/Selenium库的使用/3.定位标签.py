import time
from selenium import webdriver


driver = webdriver.Chrome(executable_path="D:/tools/chromedriver")

# driver.find_element_by_id()     # 返回一个元素
# driver.find_element_by_class_name()   # 根据类名获取元素列表
# driver.find_element_by_name()       # 根据标签的name属性返回包含标签对象元素的列表
# driver.find_element_by_xpath()      # 返回一个包含元素的列表
# driver.find_element_by_link_text()      # 根据链接文本获取元素列表
# driver.find_element_by_partial_link_text()  # 根据链接包含的文本获取元素列表
# driver.find_element_by_tag_name()   # 根据标签名获取元素列表
# driver.find_element_by_css_selector()   #根据css选择器来获取元素

url = "https://www.baidu.com"

driver.get(url)

# 通过xpath进行元素定位
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys("python")

# 通过css选择器进行元素定位
# driver.find_element_by_css_selector("#kw").send_keys("python")

# 通过name属性值进行元素定位
# driver.find_element_by_name("wd").send_keys("python")

# 通过class属性值进行元素定位
# driver.find_element_by_class_name("s_ipt").send_keys("python")

# driver.find_element_by_id("su").click()


# 通过链接文本进行元素定位
# driver.find_element_by_link_text("hao123").click()
# driver.find_element_by_partial_link_text("hao").click()

# 目标元素在当前HTML是唯一标签的时候或者是众多定位出来的标签中的第一个的时候
print(driver.find_element_by_tag_name("title"))

time.sleep(2)

driver.quit()


