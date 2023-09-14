import time

from pages.loginpage import LoginPage
from tests.BaseTest import BaseTest


class TestLogin(BaseTest):

    def test_login(self):
        time.sleep(3)
        login_page = LoginPage(self.driver)
        home_page = login_page.do_login("Admin", "admin123")
        time.sleep(3)
        assert home_page.verify_dashboard()
