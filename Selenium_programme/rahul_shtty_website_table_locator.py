from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
no_of_column=driver.find_elements(By.XPATH,"//table[@name='courses']//th") # tbody do or //(double slash)
print(len(no_of_column))
no_of_rows=driver.find_elements(By.XPATH,"//table[@name='courses']/tbody/tr")
print(len(no_of_rows))
headers_rows=driver.find_element(By.XPATH,"//table[@id='product']/thead/tr/th[1]").text
print(headers_rows)