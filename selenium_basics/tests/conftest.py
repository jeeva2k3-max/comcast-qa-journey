# conftest.py
import pytest
from utils.browser_utils import start_browser, close_browser

@pytest.fixture
def driver():
    driver = start_browser("https://example.com")
    yield driver
    close_browser(driver)
