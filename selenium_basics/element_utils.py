from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def find_element_by_id(driver, element_id, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, element_id))
    )

def find_element_by_name(driver, name, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.NAME, name))
    )

def find_elements_by_tag(driver, tag_name, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, tag_name))
    )
