from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException

#"//*[@id="q-1605310668"]/div/div/div/div/div[3]/button[2]/div[2]/div[2]/div"


service = Service(executable_path="C:/Users/yasse/Desktop/chrome developer/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()# important to make all elements available and clickable
driver.get("https://tinder.com/app/recs")
WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Log in')]"))
)
driver.find_element(By.XPATH, "//div[contains(text(), 'Log in')]").click()
WebDriverWait(driver, 1000000).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Log in with Facebook')]"))
)
driver.find_element(By.XPATH, "//div[contains(text(), 'Log in with Facebook')]").click()
original_window = driver.current_window_handle

# Wait for the new window/tab to open
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

# Get the handles of all windows
all_windows = driver.window_handles

# Switch to the new window/tab (assuming it's the last one opened)
new_window = [window for window in all_windows if window != original_window][0]
driver.switch_to.window(new_window)

# Now you can interact with the new window/tab
print(driver.title)  # Print the title of the new window/tab

# Perform actions in the new window/tab
# ...
mail = driver.find_element(By.NAME,"email")
mail.send_keys("+201110888811")
passwo = driver.find_element(By.NAME,"pass")
passwo.send_keys("Safya1990")
passwo.send_keys(Keys.ENTER)
# Switch back to the original window/tab if needed
driver.switch_to.window(original_window)
print(1)
WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Allow')]"))
)
print(2)

driver.find_element(By.XPATH, "//div[contains(text(), 'Allow')]").click()
print(3)

WebDriverWait(driver, 1000000).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Notify me')]"))
)
print(0)
# driver.find_element(By.XPATH, '//*[@id="q-1605310668"]/div/div/div/div/div[3]/button[2]/div[2]/div[2]/div').click()
driver.find_element(By.XPATH, "//div[contains(text(), 'Notify me')]").click()
print(4)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Like')]"))
)
print(5)

for i in range(50):
    print(6)
    time.sleep(3)
    WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'Hidden') and text()='Like']")))
    span_element = driver.find_element(By.XPATH, "//span[contains(@class, 'Hidden') and text()='Like']")
    driver.execute_script("arguments[0].click();", span_element) # to click non clickable elements
    print(7)


# "#q123070408 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-like-default\) > button > span > span > svg"
# "#q123070408 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-like-default\) > button > span > span > svg"
# "//*[@id="q123070408"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span/span"