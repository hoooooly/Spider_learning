from selenium import webdriver

# 实例化配置对象
options = webdriver.ChromeOptions()

# 添加配置对象
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# 创建浏览器对象，添加配置对象
driver = webdriver.Chrome(executable_path="D:/tools/chromedriver", options=options)

driver.get('https://www.baidu.com')

driver.save_screenshot("百度-无头模式.png")

driver.quit()
