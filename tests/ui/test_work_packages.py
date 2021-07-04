from time import sleep

import allure
import pytest
from config.credentials import Credentials
from framework.pages.WorkPackagesPage import WorkPackagesPage
from infra.shared_steps import SharedSteps


@allure.title('Test Creating A New Task')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_create_new_task(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    SharedSteps.login_steps(driver)

    SharedSteps.select_project_steps(driver)
    SharedSteps.goto_work_packages_steps(driver)

    work_packages_page = WorkPackagesPage(driver)
    initial_row_count = work_packages_page.count_table_rows()

    work_packages_page.create_new_task()

    work_packages_page.set_task_subject(Credentials.NEW_TASK_SUBJECT)
    work_packages_page.set_task_description(Credentials.NEW_TASK_DESCRIPTION)

    work_packages_page.save_new_task()

    work_packages_page.click_go_back_button()

    new_value = work_packages_page.count_table_rows()

    assert initial_row_count + 1 == new_value

    assert Credentials.NEW_TASK_SUBJECT == (work_packages_page.get_last_table_row())["subject"]

    assert Credentials.NEW_TASK_TYPE == work_packages_page.get_last_table_row()["type"]

#
# with allure.step('Login to OpenProject'):
#     SharedSteps.login_steps(driver)
#
# with allure.step('Go to selected project overview and choose "work packages"'):
#     SharedSteps.select_project_steps(driver)
#     SharedSteps.goto_work_packages_steps(driver)
#
# with allure.step('Note the number of rows displayed in the work packages table'):
#     work_packages_page = WorkPackagesPage(driver)
#     initial_row_count = work_packages_page.count_table_rows()
#
# with allure.step('Click "+ Create" green button and select "TASK"'):
#     work_packages_page.create_new_task()
#
# with allure.step('Fill in task subject and description'):
#     work_packages_page.set_task_subject(Credentials.NEW_TASK_SUBJECT)
#     work_packages_page.set_task_description(Credentials.NEW_TASK_DESCRIPTION)
#
# with allure.step('Click "Save" button'):
#     work_packages_page.save_new_task()
#
#
# with allure.step('Go back to work packages table and count the rows'):
#     work_packages_page.click_go_back_button()
#     new_value = work_packages_page.count_table_rows()
#
# with allure.step('Verify that a new row was added to the work packages table'):
#     assert initial_row_count + 1 == new_value
# with allure.step('Verify the subject and type of the last table row'):
#     assert Credentials.NEW_TASK_SUBJECT == (work_packages_page.get_last_table_row())["subject"]
#     assert Credentials.NEW_TASK_TYPE == work_packages_page.get_last_table_row()["type"]
