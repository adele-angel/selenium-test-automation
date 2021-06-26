import pytest
from selenium import webdriver

from pages.LoginPage import LoginPage
from utils.LogGenerator import LogGenerator
from config.credentials import TestCredentials
from config.settings import TestSettings


class TestLogin:
    logger = LogGenerator.log_generator()

    def test_login_page_title(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("--- Verifying Login Page Title")
        self.driver = setup
        self.logger.info("--- Opening URL")
        self.driver.get(TestCredentials.BASE_URL)
        actual_title = self.driver.title

        if actual_title == TestCredentials.LOGIN_PAGE_TITLE:
            self.logger.info("**** Login Page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Login Page title test failed ****")
            self.driver.save_screenshot(TestSettings.SCREENSHOT_PATH + "009_001_login_page_title.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("--- Verifying Login into user account")
        self.driver = setup
        self.logger.info("--- Opening URL")
        self.driver.get(TestCredentials.BASE_URL)
        self.login_page = LoginPage(self.driver)
        self.login_page.open_login_menu()
        self.login_page.set_username(TestCredentials.USERNAME)
        self.login_page.set_password(TestCredentials.PASSWORD)
        self.login_page.click_login()
        actual_title = self.driver.title

        if actual_title == TestCredentials.HOME_PAGE_TITLE:
            self.logger.info("**** Login Page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Login Page title test failed ****")
            self.driver.save_screenshot(TestSettings.SCREENSHOT_PATH + "009_002_home_page_title.png")
            self.driver.close()
            assert False
