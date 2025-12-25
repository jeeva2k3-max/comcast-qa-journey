from utils.browser_utils import start_browser, close_browser
from utils.assertions import assert_equal
from data.test_data import TEST_PAGES


def run_test(page):
    driver = start_browser(page["url"])
    actual_title = driver.title

    print(f"URL: {page['url']}")
    print(f"Expected title: {page['expected_title']}")
    print(f"Actual title: {actual_title}")

    assert_equal(
        actual_title,
        page["expected_title"],
        message=f"Title mismatch for URL: {page['url']}"
    )

    close_browser(driver)
    print("TEST PASSED\n")


for page in TEST_PAGES:
    try:
        run_test(page)
    except Exception as e:
        print(f"TEST FAILED ❌\nReason: {e}\n")
