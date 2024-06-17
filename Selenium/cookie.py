from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path="C:/Users/yasse/Desktop/chrome developer/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()# important to make all elements available and clickable
driver.get("https://orteil.dashnet.org/cookieclicker/")



WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID,"langSelect-EN"))
)

driver.find_element(By.ID,"langSelect-EN").click()
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "cookies"))
)

timeout = time.time() + 5*60
while True:
    buying_time = time.time() + 5
    while True:
        driver.find_element(By.ID,"bigCookie").click()
        if time.time() >= buying_time:
            score = driver.find_element(By.ID,"cookies")
            score_int = int(score.text.split()[0].replace("," , ""))
            if score_int >= 100:
                driver.find_element(By.CSS_SELECTOR,"#products #product1").click()
             
            elif score_int >= 15:
                driver.find_element(By.CSS_SELECTOR,"#products #product0").click()
            break
        
    if time.time() > timeout:
        seconds = driver.find_element(By.ID,"cookiesPerSecond")
        print(score.text)
        print(seconds.text)
        break


