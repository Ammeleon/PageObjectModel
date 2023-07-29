from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from config.config import TestData


class LoginPage(BasePage):

    """Locators"""
    LOGIN = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PAGE_TITLE = (By.xpath("//div[@class='login_logo']"))

    """Class constructor"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """Used to get page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """Used to get page status"""
    def is_page_title_exist(self):
        return self.is_visible(self.PAGE_TITLE)

    """Used to login to app"""
    def do_login(self, username, password):
        self.do_send_keys(self.LOGIN, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

