from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Gopal")
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
alert = driver.switch_to.alert
message = alert.text
print(message)
assert "Gopal" in message
alert.accept()
#alert.dismiss()
time.sleep(2)