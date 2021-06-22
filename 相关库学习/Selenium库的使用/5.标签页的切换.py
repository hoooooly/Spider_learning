import time
from selenium import webdriver

url = "https://sz.58.com/"

driver = webdriver.Chrome(executable_path="D:/tools/chromedriver")

driver.get(url)

print(driver.current_url)
print(driver.window_handles)

# 定位并点击租房按钮
driver.find_element_by_xpath('//*[@id="fcNav"]/em/a[1]').click()


print(driver.current_url)
print(driver.window_handles)

time.sleep(3)
current_windows = driver.window_handles

driver.switch_to.window(current_windows[0])

time.sleep(3)

driver.quit()
