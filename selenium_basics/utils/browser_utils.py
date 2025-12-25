from selenium import webdriver

def start_browser(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def close_browser(driver):
    driver.quit()

if __name__ == "__main__":
    driver = start_browser("https://example.com")
    print("Title:", driver.title)
    close_browser(driver)
