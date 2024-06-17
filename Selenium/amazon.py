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

driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
time.sleep(10)
# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "a-section a-spacing-none aok-align-center aok-relative"))
# )

div_element = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-none.aok-align-center.aok-relative') #find all elements with this selector
input_element = driver.find_element(By.CSS_SELECTOR, 'span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay span.a-offscreen').text #find first elemnt with this span selsector 
offscreen_span = driver.find_element(By.CSS_SELECTOR, 'span.aok-offscreen')
print(offscreen_span.text.strip())
price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
print(price)

# price = driver.find_element(By.NAME, "whatevername").tag_name
# price = driver.find_element(By.ID, "whateverID")..get_attribute()
price_xpath = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]').text # we use copy options in the inspector should use '' not ""
print(price_xpath)
# input_element.clear()
# input_element.send_keys("tech with tim" + Keys.ENTER)
# an example of copy selector from inspect "#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.aok-offscreen"
print("hi")
print(input_element)

# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
# )

# link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
# link.click()

time.sleep(10)

driver.quit()