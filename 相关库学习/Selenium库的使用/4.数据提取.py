import time
from selenium import webdriver


driver = webdriver.Chrome(executable_path="D:/tools/chromedriver")

driver.get("https://holychan.ltd/")

title = driver.find_element_by_tag_name("h2")

print(title.text)
# Holy的个人站点

email = driver.find_element_by_xpath("//*[@id='footer']/div[2]/div/div/ul[1]/li/a")

print(email.get_attribute('href'))
# mailto:espholychan@outlook.com

driver.quit()
