from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

# Wait for page title
WebDriverWait(driver, 10).until(EC.title_is("Example Domain"))

title = driver.title
print("Page title:", title)

if title == "Example Domain":
    print("TEST PASSED")
else:
    print("TEST FAILED")

driver.quit()
