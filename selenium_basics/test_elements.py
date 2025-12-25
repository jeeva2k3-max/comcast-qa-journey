from reusable_browser import start_browser, close_browser
from element_utils import find_elements_by_tag

driver = start_browser("https://example.com")

elements = find_elements_by_tag(driver, "h1")
print("Found elements:", len(elements))

close_browser(driver)
