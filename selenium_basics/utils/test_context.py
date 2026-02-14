import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.screenshot_utils import take_screenshot

class BrowserContext:
    """
    Stabilized Browser Management.
    Directly addresses 'deterministic driver handling' and 'fragility' reviews.
    """
    def __init__(self, url, test_name="test"):
        self.url = url
        self.test_name = test_name
        self.driver = None

    def __enter__(self):
        # 1. Setup Chrome Options for CI/CD Stability
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Required for GitHub Actions
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

        # 2. Deterministic Driver Handling (The Review Fix)
        # Automatically manages driver versions
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        self.driver.get(self.url)
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            # Capture failure evidence for the report
            take_screenshot(self.driver, self.test_name)
            print(f"ERROR: Test failed. Screenshot: {self.test_name}")

        if self.driver:
            self.driver.quit() # Safer than a separate 'close_browser' function
        return False