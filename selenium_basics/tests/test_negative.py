import pytest
from utils.test_context import BrowserContext

# Parametrization handles multiple "Negative" cases in one function
@pytest.mark.parametrize("user, pw, expected_error", [
    ("invalid_user", "wrong_pass", "Your username is invalid!"),
    ("", "SuperSecretPassword!", "Your username is invalid!"), # Empty user case
    ("tomsmith", "wrong_pass", "Your password is invalid!")    # Wrong password case
])
def test_negative_login_validation(user, pw, expected_error):
    """
    Addresses Review: 'Replace placeholder test with real UI validations.'
    This test ensures the system handles 'bad' data gracefully.
    """
    target_url = "https://the-internet.herokuapp.com/login"
    
    with BrowserContext(target_url, test_name=f"neg_login_{user}") as driver:
        # 1. Locate elements and input data
        driver.find_element("id", "username").send_keys(user)
        driver.find_element("id", "password").send_keys(pw)
        
        # 2. Trigger Action
        driver.find_element("css selector", "button.radius").click()
        
        # 3. Real UI Validation: The "Signal"
        # We check the 'flash' message text specifically.
        error_msg_element = driver.find_element("id", "flash")
        actual_text = error_msg_element.text
        
        # Use 'in' because the flash message often contains extra characters/icons
        assert expected_error in actual_text, \
            f"SIGNAL FAILURE: Expected error '{expected_error}' not found in '{actual_text}'"