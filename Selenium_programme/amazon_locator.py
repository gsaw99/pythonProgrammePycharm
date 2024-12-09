from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, "//a[text()='Sell']").click()
driver.find_element(By.XPATH, "//input[@type='text' and @id='twotabsearchtextbox']").send_keys("Tshirts")
driver.find_element(By.XPATH, "//div[@class='s-suggestion s-suggestion-ellipsis-direction' and @aria-label='tshirt for men']").click()
time.sleep(2)






# )