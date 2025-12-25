from utils.browser_utils import start_browser, close_browser


class TestContext:
    def __init__(self, url):
        self.url = url
        self.driver = None

    def __enter__(self):
        self.driver = start_browser(self.url)
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        close_browser(self.driver)
        if exc_type:
            print(f"Test exited due to error: {exc_val}")
        return False
