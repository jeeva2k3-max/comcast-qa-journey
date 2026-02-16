import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
def test_example_title(driver):
    # Step 1: Explicitly navigate (since we removed it from start_browser)
    url = "https://example.com"
    driver.get(url)
    
    # Step 2: GOGGINS LEVEL HARDENING - Don't just assert, WAIT.
    # We wait up to 10 seconds for the title to contain 'Example'
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains("Example"))
    
    # Step 3: Now the assertion is guaranteed to pass or timeout cleanly
    assert "Example Domain" in driver.title