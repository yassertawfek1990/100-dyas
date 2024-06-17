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

driver.get("https://www.python.org/")

#"#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li:nth-child(1)"
selector = "#content  div  section  div.list-widgets.row  div.medium-widget.event-widget.last div  ul  li"

dic = {}

li = driver.find_elements(By.CSS_SELECTOR,selector)
print(len(li))
n = 0
for i in li:
    sub_dic = {}
    sub_dic["time"] = i.text.split("\n")[0]
    sub_dic["name"] = i.text.split("\n")[1]
    dic[n] = sub_dic
    n +=1

print(dic)
