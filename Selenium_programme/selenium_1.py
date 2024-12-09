# Static dropdown ka locator element  hamesha select class ke under rahega jab inspect karenge

import time
from select import select
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

serv_obj=Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
driver.maximize_window()
driver.refresh()
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//input[@id='name']").send_keys('gopal')
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("gopalsaw90@gmail.com")
male=driver.find_element(By.XPATH, "//input[@id='gender']")
print(male.is_selected()) # False,Abhi select nahi tha isliye False aya,ab same locator ma click method use karke select karenge
driver.find_element(By.XPATH, "//input[@id='gender']").click()

print(male.is_selected()) # True
driver.find_element(By.XPATH, "//input[@class='form-check-input mt-0']").click()
driver.find_element(By.XPATH, "//input[@id='mobile']").send_keys(8553573847)
driver.find_element(By.CSS_SELECTOR, 'input#dob').send_keys(15-10-1990)
checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox']")
time.sleep(3)
for checkbox in checkboxes:
    checkbox.click()

driver.find_element(By.XPATH, "//textarea[@placeholder='Currend Address']").send_keys("Jharia Dhanbad")
try:
  sel_state = Select(driver.find_element(By.XPATH, "//select[@id='state']")) # dropdown box ka element hai ye jo ki Select class ke under define hoga.
  #sel_state.select_by_visible_text("NCR") # jo dropdown ma item hai , usko bracket ma daalte hain
  sel_state.select_by_index(2)
  #sel_state.select_by_value("") # locators ma job bhi select class ke under
                                # value= jo bhi hoga wahi value bracket ma daalna hoga
except NoSuchElementException:
   print("please find correct locator")

finally:
    print("success")

sel_city = Select(driver.find_element(By.XPATH, "//select[@id='city']"))
sel_city.select_by_visible_text("Agra")
#sel_city.select_by_index(2)
#sel_city.select_by_value("4")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

time.sleep(5)
driver.close()
