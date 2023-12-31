import pytest

from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from config.config import TestData



class Test_Login(BaseTest):

    def test_login_page_title_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_page_title_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
