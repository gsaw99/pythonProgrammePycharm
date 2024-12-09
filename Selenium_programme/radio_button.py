from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
radio_buttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton") # Hamlog radio button ka bhi common element lekar phir ek-ek ko click kar sakte hain
radio_buttons[1].click() # 1 is a index of radio button
assert radio_buttons[1].is_selected()
time.sleep(2)