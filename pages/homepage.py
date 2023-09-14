from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    dashboardEle = (By.XPATH, "//h6[normalize-space()='Dashboard']")

    def verify_dashboard(self):
        return self.is_visible(self.dashboardEle)

