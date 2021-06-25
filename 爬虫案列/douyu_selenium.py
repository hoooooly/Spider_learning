# coding:utf-8
import time
import json
from selenium import webdriver


class Douyu(object):
    def __init__(self):
        # 实例化配置对象
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54')
        self.url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome('D:/tools/chromedriver')

    def parse_data(self):
        room_list = self.driver.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li/div')
        # print(len(room_list)) #120
        # 遍历房间列表，继续查找信息
        data_list = []
        for room in room_list:
            temp = {}
            temp['title'] = room.find_element_by_xpath('./a/div[2]/div[1]/h3').text
            temp['type'] = room.find_element_by_xpath('./a/div[2]/div[1]/span').text
            temp['owner'] = room.find_element_by_xpath('./a/div[2]/div[2]/h2/div').text
            temp['num'] = room.find_element_by_xpath('./a/div[2]/div[2]/span').text
            temp['img_src'] = room.find_element_by_xpath('./a/div[1]/div[1]/img').get_attribute("src")
            data_list.append(temp)
        return data_list

    def save_data(self, data_list):
        for data in data_list:
            print(data)

    def run(self):
        # url
        # driver
        # get
        self.driver.get(self.url)
        time.sleep(1)
        print(self.driver.find_element_by_xpath('//*[@id="listAll"]/section[2]/div[2]/div/ul/li[9]').get_attribute("aria-disabled"))
        while True:
            # parse
            data_list = self.parse_data()
            # save
            self.save_data(data_list)
            # next
            if self.driver.find_element_by_xpath('//*[@id="listAll"]/section[2]/div[2]/div/ul/li[9]').get_attribute("aria-disabled") == "false":
                # 模拟人为下拉
                self.driver.execute_script('scrollTo(0,10000)')
                self.driver.find_element_by_xpath('//*[@id="listAll"]/section[2]/div[2]/div/ul/li[9]').click()
                time.sleep(1)
            else:
                # close
                self.driver.quit()


if __name__ == '__main__':
    douyu = Douyu()
    douyu.run()
