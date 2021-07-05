"""
Test 010 - UI - Create Task

Prerequisites:
    A project named "TestProject1" already exists

Steps:
    1. Login to OpenProject
    2. On "Home" page, top-left corner, click "Select a project" menu button, and select "TestProject1" from the drop-down
    3. On the "Project Overview" page, left side menu, click "Work packages". Once on the "Work packages" page, note the number of rows displayed in the work packages table.
    4. Click "+ Create" green button and select "TASK"
    5. Verify the text "New TASK" on top of the form that got opened on the right side
    6. Type unique strings into the subject and description boxes
    7. Click "Save" button
    8. Verify that a new row was added to the work packages table
    9. Verify the subject and type of the last table row
"""

import pytest
import allure
from config.credentials import Credentials
from framework.pages.WorkPackagesPage import WorkPackagesPage
from infra.shared_steps import SharedSteps


@allure.title("Test Creating A New Task")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.test_010
@pytest.mark.task
def test_010_create_task(setup):
    with allure.step("setup driver"):
        driver = setup
        driver.get(Credentials.BASE_URL)

    # step 1
    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    # step 2
    with allure.step('Click "Select a project" menu button, and select "TestProject1" from the drop-down'):
        SharedSteps.select_project_steps(driver)

    # step 3
    with allure.step('On the "Project Overview" page, left side menu, click "Work packages"'):
        SharedSteps.goto_work_packages_steps(driver)
    with allure.step('Create a WorkPackagesPage instance'):
        work_packages_page = WorkPackagesPage(driver)
    with allure.step('Note the number of rows displayed in the work packages table'):
        initial_row_count = work_packages_page.count_table_rows()

    # step 4
    with allure.step('Click "+ Create" green button and select "TASK"'):
        work_packages_page.create_new_task()

    # step 5
    with allure.step('Verify the text "New TASK" on top of the form that got opened on the right side'):
        assert work_packages_page.get_work_package_form_title() == Credentials.WORK_PACKAGE_FORM_TITLE

    # step 6
    with allure.step('Type unique strings into the subject and description boxes'):
        work_packages_page.set_task_subject(Credentials.NEW_TASK_SUBJECT)
        work_packages_page.set_task_description(Credentials.NEW_TASK_DESCRIPTION)

    # step 7
    with allure.step('Click "Save" button'):
        work_packages_page.save_new_task()
    with allure.step('Go back to "Work Packages" page'):
        work_packages_page.click_go_back_button()

    # step 8
    with allure.step('Verify that a new row was added to the work packages table'):
        current_row_count = work_packages_page.count_table_rows()
        assert initial_row_count + 1 == current_row_count

    # step 9
    with allure.step('Verify the subject and type of the last table row'):
        assert Credentials.NEW_TASK_SUBJECT == work_packages_page.get_last_table_row()["subject"]
        assert Credentials.NEW_TASK_TYPE == work_packages_page.get_last_table_row()["type"]
