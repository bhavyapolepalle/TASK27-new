import pytest
from datetime import datetime
from pages.login_page import LoginPage
from utils import read_test_data, write_test_result

@pytest.mark.parametrize("test_id, username, password, date, time, tester, result", read_test_data('test_data.xlsx'))
def test_login(driver, test_id, username, password, date, time, tester, result):
    login_page = LoginPage(driver)
    login_page.load()

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    if login_page.is_login_successful():
        test_result = "Test Passed"
    else:
        test_result = "Test Failed"

    write_test_result('test_data.xlsx', test_id + 1, test_result)

    assert test_result == "Test Passed"