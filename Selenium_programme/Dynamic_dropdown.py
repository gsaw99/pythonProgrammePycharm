# No select class used in dynamic dropdown
# First we will inspect item box element
# We will create common Xpath for dropdown item


from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID,'autosuggest').send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a") # created common Xpath (used parent to child ), yahan pe isliye common elemnet liye q ki future ma ho sakta hai ki 'india' element same number pe na ho.
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break # jaise hi isko India milega, break ho jayega.
time.sleep(2)
#print(driver.find_element(By.ID,'autosuggest').get_attribute('value')) # when you need dynamic value
# (jo dikhta nahi UI ma or jo dropdown ma type karne se ata ho) then we use get_attribute

assert driver.find_element(By.ID,'autosuggest').get_attribute('value') == "India"