from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://sites.google.com/chromium.org/driver/

service = Service(executable_path="C:/Users/yasse/Desktop/chrome developer/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com")
time.sleep(10)
name = driver.find_element(By.NAME,"fName")
name.send_keys("Safya")
name.send_keys(Keys.ENTER)
lname = driver.find_element(By.NAME,"lName")
lname.send_keys("Hamdy")
lname.send_keys(Keys.ENTER)
email = driver.find_element(By.NAME,"email")
email.send_keys("safia18.hamdi@gmail.com")
email.send_keys(Keys.ENTER)
submit = driver.find_element(By.CLASS_NAME,"btn btn-lg btn-primary btn-block")
submit.click()