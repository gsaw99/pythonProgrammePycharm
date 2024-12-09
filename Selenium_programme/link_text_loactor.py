import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.amazon.in/")
driver.maximize_window()
#driver.find_element(By.LINK_TEXT,"Amazon miniTV").click()
try:
 driver.find_element(By.PARTIAL_LINK_TEXT,"Amazon min").click()
except NoSuchElementException:
    print("Element Not Found")
finally:
    driver.close()

time.sleep(2)
