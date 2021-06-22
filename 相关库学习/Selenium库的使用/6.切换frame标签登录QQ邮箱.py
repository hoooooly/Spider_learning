import time
from selenium import webdriver

url = "https://mail.qq.com/"

driver = webdriver.Chrome(executable_path="D:/tools/chromedriver")

driver.get(url)

# 切换当登陆的frame
driver.switch_to.frame('login_frame')

# 输入账号
driver.find_element_by_xpath('//*[@id="u"]').send_keys("2472811778")
# 输入密码
driver.find_element_by_xpath('//*[@id="p"]').send_keys("Holychan_1314520")
# 点击登录
driver.find_element_by_xpath('//*[@id="login_button"]').click()

time.sleep(2)
# 输入独立密码
driver.find_element_by_xpath('//*[@id="pp"]').send_keys("Holy845620")

# 点击登录
driver.find_element_by_xpath('//*[@id="btlogin"]').click()

time.sleep(6)

driver.quit()

