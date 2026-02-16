import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def start_browser():
    chrome_options = Options()
    
    # READ FROM ENVIRONMENT VARIABLE (For CI/CD)
    # If running in GitHub Actions, it sets CI=true automatically
    if os.getenv('CI') == 'true':
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    return driver

def close_browser(driver):
    if driver:
        driver.quit()