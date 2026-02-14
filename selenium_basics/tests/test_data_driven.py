import pytest
from utils.test_context import BrowserContext  # Fixed naming consistency
from data.test_data import TEST_PAGES

@pytest.mark.parametrize("page", TEST_PAGES)
def test_page_titles(page):
    """
    MNC Standard: Parametrized test that treats each URL as a unique test case.
    This satisfies the 'Signal-to-Noise' and 'Pytest Function' review points.
    """
    # Use BrowserContext (ensure this matches your class name in utils)
    with BrowserContext(
        page["url"], 
        test_name=page["url"].replace("https://", "").replace("/", "_")
    ) as driver:
        
        actual_title = driver.title
        expected_title = page["expected_title"]

        # Professional Assertion: No more custom print statements for pass/fail
        # Pytest handles the reporting for you.
        assert actual_title == expected_title, f"Title mismatch at {page['url']}! Expected '{expected_title}', got '{actual_title}'"