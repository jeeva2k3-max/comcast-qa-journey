from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

try:
    # Wait until search results are present
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3"))
    )

    results[0].click()

    # Validate page title
    title = driver.title
    print("Page title:", title)

    if "Selenium" in title:
        print("TEST PASSED")
    else:
        print("TEST FAILED")

except Exception as e:
    print("TEST FAILED due to exception:", e)

driver.quit()
