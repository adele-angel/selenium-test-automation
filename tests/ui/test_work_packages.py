import allure
import pytest
from config.credentials import Credentials
from framework.pages.WorkPackagesPage import WorkPackagesPage
from infra.shared_steps import SharedSteps


@allure.title('Test navigation into "Work Packages" page')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
def test_verify_project_name(setup):
    with allure.step('setup driver'):
        driver = setup
        driver.get(Credentials.BASE_URL)

    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    with allure.step('Click "Select a project" menu button, and select a project from the drop-down'):
        SharedSteps.select_project_steps(driver)

    with allure.step('On the "Project Overview" page, left side menu, click "Work packages"'):
        SharedSteps.goto_work_packages_steps(driver)

    with allure.step("Check if webpage title is correct"):
        assert driver.title == Credentials.WORK_PACKAGES_PAGE_TITLE.format(Credentials.HOME_PAGE_SELECTED_PROJECT)


@allure.title('Test creating a new task')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.test_010
def test_create_new_task(setup):
    with allure.step("setup driver"):
        driver = setup
        driver.get(Credentials.BASE_URL)

    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    with allure.step('Go to selected project overview'):
        SharedSteps.select_project_steps(driver)

    with allure.step('Choose "work packages"'):
        SharedSteps.goto_work_packages_steps(driver)

    with allure.step('Create a WorkPackagesPage instance'):
        work_packages_page = WorkPackagesPage(driver)

    with allure.step('Note the number of rows displayed in the work packages table'):
        initial_row_count = work_packages_page.count_table_rows()

    with allure.step('Click "+ Create" green button and select "TASK"'):
        work_packages_page.create_new_task()

    with allure.step("Check if webpage title is correct"):
        assert driver.title == Credentials.NEW_WORK_PACKAGE_PAGE_TITLE.format(Credentials.HOME_PAGE_SELECTED_PROJECT)

    with allure.step('Fill in task subject and description'):
        work_packages_page.set_task_subject(Credentials.NEW_TASK_SUBJECT)
        work_packages_page.set_task_description(Credentials.NEW_TASK_DESCRIPTION)

    with allure.step('Click "Save" button'):
        work_packages_page.save_new_task()

    with allure.step("Check if webpage title is correct"):
        assert driver.title == Credentials.CREATED_TASK_PAGE_TITLE.format(Credentials.HOME_PAGE_SELECTED_PROJECT)

    with allure.step('Go back to work packages table and count the rows'):
        work_packages_page.click_go_back_button()
        new_value = work_packages_page.count_table_rows()

    with allure.step('Verify that a new row was added to the work packages table'):
        assert initial_row_count + 1 == new_value

    with allure.step('Verify the subject and type of the last table row'):
        assert Credentials.NEW_TASK_SUBJECT == work_packages_page.get_last_table_row()["subject"]
        assert Credentials.NEW_TASK_TYPE == work_packages_page.get_last_table_row()["type"]
