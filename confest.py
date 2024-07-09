import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()  # or use any other browser driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()