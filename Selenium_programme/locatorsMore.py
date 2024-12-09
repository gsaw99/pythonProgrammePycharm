from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()

time.sleep(3)