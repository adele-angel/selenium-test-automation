import pytest
import re

from selenium import webdriver

from pages.HomePage import HomePage
from pages.NewProjectPage import NewProjectPage
from pages.LoginPage import LoginPage
from utils.LogGenerator import LogGenerator
from config.credentials import TestCredentials
from config.settings import TestSettings


class TestNewProject:
    logger = LogGenerator.log_generator()

    def test_create_new_project(self, setup):
        self.logger.info("*************** Test_004 New Project *****************")
        self.driver = setup
        self.logger.info("--- Opening URL")
        self.driver.get(TestCredentials.BASE_URL)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(TestCredentials.USERNAME)
        self.login_page.set_password(TestCredentials.PASSWORD)
        self.login_page.click_login()
        self.logger.info("-- Login successful")

        self.home_page = HomePage(self.driver)
        self.home_page.click_new_project()

        self.logger.info("--- Starting add new project test")
        self.new_project_page = NewProjectPage(self.driver)
        self.logger.info("--- Providing project details")
        self.new_project_page.set_project_name(TestCredentials.NEW_PROJECT_NAME)
        self.new_project_page.click_advanced_settings()
        self.new_project_page.set_project_description(TestCredentials.NEW_PROJECT_DESCRIPTION)
        self.new_project_page.set_status(TestCredentials.NEW_PROJECT_STATUS)
        self.new_project_page.create_new_project()
        self.logger.info("--- Saving new project")
        self.logger.info("--- New project validation started")

        project_name = self.new_project_page.set_project_name(TestCredentials.NEW_PROJECT_NAME)

        if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)” + “(?=.*[-+_!@#$%^&*., ?]).+$", project_name):
            self.logger.info("**** Project name test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Project name test test failed ****")
            self.driver.save_screenshot(TestSettings.SCREENSHOT_PATH + "009_004_new_project_page_create.png")
            self.driver.close()
            assert False