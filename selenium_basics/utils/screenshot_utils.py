import os
from datetime import datetime


def take_screenshot(driver, test_name):
    screenshots_dir = "screenshots"

    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(screenshots_dir, filename)

    driver.save_screenshot(filepath)
    print(f"Screenshot saved: {filepath}")
