import pytest

@pytest.mark.smoke
def test_example_title(driver):
    assert "Example Domain" in driver.title
