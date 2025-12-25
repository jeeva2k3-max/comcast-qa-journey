from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

time.sleep(3)

# Find all search result links
results = driver.find_elements(By.CSS_SELECTOR, "h3")

# Click the first result if exists
if results:
    results[0].click()
    print("Clicked first search result")
else:
    print("No results found")

time.sleep(5)
driver.quit()
