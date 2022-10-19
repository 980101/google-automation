from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

# URL 접속
driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdkZ2GsolQhQhAYb9tHeyvkFtXJiPk-28vV81ysA-bzjy0lkg/viewform")

# 응답자이름 입력
name_elem = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
time.sleep(1)
name_elem.send_keys(Keys.RETURN)
time.sleep(1)
name_elem.send_keys("홍길동")

# 만족도 입력
place_elem = driver.find_element_by_xpath('//*[@id="i9"]/div[3]/div').click()

# 응답시간 입력
time.sleep(1)
time_elem = driver.find_element_by_xpath('//*[@id="i28"]/div[3]/div').click()

# 응답시 특이사항 입력
time.sleep(1)
note_elem = driver.find_element_by_xpath('//*[@id="i47"]/div[3]/div').click()

# 제출하기
submit_elem = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
submit_elem.click()

driver.close()
