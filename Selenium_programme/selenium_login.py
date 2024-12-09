from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

serv_obj=Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.tutorialspoint.com/selenium/practice/register.php")
driver.maximize_window()
#driver.refresh()
time.sleep(3)
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//input[@id='firstname']").send_keys("Gopal Kumar")
driver.find_element(By.XPATH, "//input[@id='lastname']").send_keys("Saw")
driver.find_element(By.XPATH, "//input[@placeholder='UserName']").send_keys("gopal123")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("gopal@1234")
driver.find_element(By.XPATH, "//input[@value='Register']").click()