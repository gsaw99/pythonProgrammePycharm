from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
time.sleep(2)
print(len(checkboxes))
'''for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2": # get_attribute ke bracket ma attribute fill karna hai,jis attribute ka value chaiye usi ka
        checkbox.click()
        assert checkbox.is_selected() # it is used for selected or not(True or False)
        break'''

# Select all the checkbox
'''for checkbox in checkboxes:
    checkbox.click()'''
# Select first 2 checkboxes
'''for checkbox in range(len(checkboxes)):
    if checkbox<2:
     checkboxes[checkbox].click()'''
# Select last 2 checkboxes
for checkbox in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[checkbox].click()

# Clearing all the checkboxes
'''for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()'''
time.sleep(3)

'''wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located())'''