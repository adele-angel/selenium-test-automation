import allure
from allure_commons.types import AttachmentType

from config.credentials import Credentials


def get_screenshot(driver, test, reason, expected_value=None, actual_value=None):
    file_name = f'test_{test}_{reason}_screenshot'
    allure.attach(driver.get_screenshot_as_png(), name=file_name, attachment_type=AttachmentType.PNG)
    if reason == "page_title":
        return f'\nPage title not as expected:\n"{driver.title}" ≠ "{expected_value}"\n'
    elif reason == "identifier":
        return f'\nProject identifier not as expected:\n"{expected_value}" is not in {driver.current_url}\n'
    elif reason == "unique":
        return f'\n"{actual_value}" is not a unique string\nIt must contain letters (upper & lower case), numbers, spaces and some special characters\n'
    elif reason == "name":
        return f'\nSelected project name not as expected:\n"{actual_value}" ≠ "{expected_value}"\n'
    elif reason == "form_title":
        return f'\nForm title not as expected:\n"{actual_value}" ≠ "{expected_value}"\n'
    elif reason == "row_count":
        return f'\nFailed to add row to work packages table:\n"{actual_value}" + 1 ≠ "{expected_value}"\n'
    elif reason == "task_type":
        return f'\nTask type not as expected:\n"{actual_value}" ≠ "{expected_value}"\n'
    elif reason == "task_subject":
        return f'\nTask subject not as expected:\n"{actual_value}" ≠ "{expected_value}"\n'
    elif reason == "login":
        return f'\nFailed to log into OpenProject app\n'
    else:
        return f'\nAssertion failed for some reason...\n'
