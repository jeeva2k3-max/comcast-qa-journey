from reusable_browser import start_browser, close_browser
from test_data import TEST_PAGES

def run_test(page):
    driver = start_browser(page["url"])
    actual_title = driver.title
    print(f"URL: {page['url']}")
    print(f"Expected: {page['expected_title']}")
    print(f"Actual: {actual_title}")

    if page["expected_title"] == actual_title:
        print("TEST PASSED\n")
    else:
        print("TEST FAILED\n")

    close_browser(driver)

for page in TEST_PAGES:
    run_test(page)
