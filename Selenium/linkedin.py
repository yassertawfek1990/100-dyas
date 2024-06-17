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
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3941906286&f_AL=true&geoId=105072130&keywords=inside%20sales%20representative&location=Poland&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true")

# "#ember194 > span:nth-child(1)"
# "#ember173"
#"j//*[@id="ember1057"]"

# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.ID,"#ember194 > span:nth-child(1)"))
# )

# print(driver.find_element(By.ID,"#ember194 > span:nth-child(1)").text)


username = "dr.yassertawfek@gmail.com"
pass_word = "01003931200"
driver.find_element(By.LINK_TEXT, "Sign in").click()
name = driver.find_element(By.ID,"username")
name.send_keys(username)
# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.ID,"password"))
# )
password = driver.find_element(By.ID,"password")
password.send_keys(pass_word)
password.send_keys(Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,".job-card-container__link"))
)
cards = driver.find_elements(By.CSS_SELECTOR, ".job-card-container__link")
for i in cards:
    try:
        i.click()
        driver.find_element(By.CLASS_NAME,"jobs-apply-button").click()
        print(1)
        driver.find_element(By.XPATH, "//span[contains(@class, 'artdeco-button__text') and text()='Next']").click()
        print(1)
    
        driver.find_element(By.XPATH, "//span[contains(@class, 'artdeco-button__text') and text()='Next']").click()
        print(1)
        driver.find_element(By.XPATH, "//span[contains(@class, 'artdeco-button__text') and text()='Review']").click()

        print(1)
        driver.find_element(By.XPATH, "//span[contains(@class, 'artdeco-button__text') and text()='Submit application']").click()

        print(1)
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

