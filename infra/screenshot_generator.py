import os
import uuid
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from config.settings import Settings

# TODO: Add screenshot on failed assertion with allure
# def get_screenshot(driver, file_name):
#     allure.attach(driver.get_screenshot_as_png(), name=file_name, attachment_type=allure.attachment_type.PNG)


def _capture_screenshot(driver: WebDriver):
    file_name = Settings.SCREENSHOTS_PATH + '\\' + str(uuid.uuid1()) + '.png'
    driver.get_screenshot_as_file(file_name)
    return file_name


def save_capture(driver: WebDriver, name: str):
    file_name = _capture_screenshot(driver)
    if os.path.exists(file_name):
        allure.attach.file(file_name, attachment_type=allure.attachment_type.PNG, name=name)
