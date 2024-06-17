from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException



service = Service(executable_path="C:/Users/yasse/Desktop/chrome developer/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()# important to make all elements available and clickable
driver.get("https://www.speedtest.net")
print(1)
start = driver.find_element(By.CLASS_NAME,"start-text")
print(start.text)
print(2)
start.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"result-data-large number result-data-value download-speed"))
)
print(0)
download = driver.find_element(By.CLASS_NAME,"download-speed").text
print(3)
print(download)
upload = driver.find_element(By.CLASS_NAME,"upload-speed").text
print(4)
print(upload)

#"#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span"

use = "yasser89788462"
pw = "01003931200"
promised_down = 150
promised_up = 10

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.promised_down = 150
        self.promised_up = 10

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass