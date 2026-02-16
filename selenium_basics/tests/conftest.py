import pytest
from utils.browser_utils import start_browser, close_browser
from utils.screenshot_utils import take_screenshot

@pytest.fixture(scope="function")
def driver():
    # We will eventually move the URL to a config or test data file
    driver = start_browser() 
    yield driver
    close_browser(driver)

@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Extends the Pytest report to take a screenshot on failure.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        # Access the driver from the test fixture
        driver_fixture = item.funcargs.get('driver')
        if driver_fixture:
            screenshot_name = f"fail_{item.name}"
            take_screenshot(driver_fixture, screenshot_name)