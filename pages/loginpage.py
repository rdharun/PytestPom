from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.homepage import HomePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    EMAIL = (By.XPATH, "//input[@name = 'username']")
    PASSWORD = (By.XPATH, "//input[@name = 'password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")

    def do_login(self, userName, passWord):
        self.do_sendkeys(self.EMAIL, userName)
        self.do_sendkeys(self.PASSWORD, passWord)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)
