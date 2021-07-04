import allure
from allure_commons.types import AttachmentType


# TODO: config file path
def get_screenshot(driver, file_name):
    allure.attach(driver.get_screenshot_as_png(), name=file_name, attachment_type=AttachmentType.PNG)
