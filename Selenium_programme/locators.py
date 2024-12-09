from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME, 'email').send_keys("gsaw997387@gmail.com")
driver.find_element(By.ID, 'exampleInputPassword1').send_keys("1234567")
driver.find_element(By.ID, 'exampleCheck1').click()

# XPATH=//TagName[@attributes='value']--> //input[@type='submit']
# CSS= TagName[attributes='value']--> input[name='name'], #id, .class
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Gopal")
driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, 'alert-success').text # Agar classnmae locator ke element ma space
                                                            # ho to iska matlab usme multile class element hai,
                                                            #koi bhi ek element lelo
print(message)
assert "success" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello again")

time.sleep(3)
