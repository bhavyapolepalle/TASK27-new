from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def load(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        username_field = self.find_element(By.NAME, 'username')
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.find_element(By.NAME, 'password')
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()

    def is_login_successful(self):
        try:
            self.find_element(By.ID, 'account-name')
            return True
        except:
            return False