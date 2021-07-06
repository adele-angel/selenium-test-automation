import allure
from config.settings import Settings


def assert_msg_generator(test_type, test_name, action, obj, attr, expected, actual, driver):
    if test_type == "ui" and driver is not None:
        allure.attach(driver.get_screenshot_as_png(), name=Settings.SCREENSHOTS_PATH + test_name, attachment_type=allure.attachment_type.PNG)
    return f'Failed to get {action} {obj} {attr}: {expected} ≠ {actual}'


"""
test_type = ui, api
action = match, correct, get, send
obj = status_code, project_name, project_desc, project_identifier, task_type, task_subject, lock_version
attr = 
"""
