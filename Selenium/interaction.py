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

driver.get("https://en.wikipedia.org/wiki/Main_Page")
time.sleep(10)
link = driver.find_element(By.PARTIAL_LINK_TEXT,"anyone").text
print(link)
articles = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
articles.click()
search = driver.find_element(By.NAME,"search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

