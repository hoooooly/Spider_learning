import time
from selenium import webdriver

url = "https://www.baidu.com/"

driver = webdriver.Chrome(executable_path="D:/tools/chromedriver")

driver.get(url)

print(driver.get_cookies())

cookies_dict = {cookie['name']:cookie['value'] for cookie in driver.get_cookies()}

print(cookies_dict)
driver.quit()