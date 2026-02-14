from utils.browser_utils import start_browser, close_browser
from utils.screenshot_utils import take_screenshot


class BrowserContext:

    def __init__(self, url, test_name="test"):
        self.url = url
        self.test_name = test_name
        self.driver = None

    def __enter__(self):
        self.driver = start_browser(self.url)
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            take_screenshot(self.driver, self.test_name)
            print(f"Test failed. Screenshot captured for {self.test_name}")

        close_browser(self.driver)
        return False
