from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Find the search box by NAME
search_box = driver.find_element(By.NAME, "q")

# Type text
search_box.send_keys("Selenium Python")

# Press ENTER
search_box.send_keys(Keys.RETURN)

# Wait to see results
time.sleep(5)

driver.quit()
