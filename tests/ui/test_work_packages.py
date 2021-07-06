import allure
import pytest
from config.credentials import Credentials
from framework.pages.WorkPackagesPage import WorkPackagesPage
from infra.screenshot_generator import get_screenshot
from infra.shared_steps import SharedSteps


@allure.title('Test navigation into "Work Packages" page')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.sanity
@pytest.mark.work_packages
def test_work_package_page_title(setup):
    with allure.step('Setup driver'):
        driver = setup
        driver.get(Credentials.BASE_URL)

    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    with allure.step('Click "Select a project" menu button, and select a project from the drop-down'):
        SharedSteps.select_project_steps(driver)

    with allure.step('On the "Project Overview" page, left side menu, click "Work packages"'):
        SharedSteps.goto_work_packages_steps(driver)

    with allure.step("Check if webpage title is correct"):
        expected_title = Credentials.WORK_PACKAGES_PAGE_TITLE_1.format(Credentials.HOME_PAGE_SELECTED_PROJECT)
        assert driver.title == expected_title, get_screenshot(driver, "work_packages", "page_title", expected_title)


@allure.title('Test creating a new task')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.sanity
@pytest.mark.work_packages
@pytest.mark.task
def test_create_new_task(setup):
    with allure.step('Setup driver'):
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

    with allure.step('Check if webpage title is correct'):
        expected_title = Credentials.WORK_PACKAGES_PAGE_TITLE_2.format(Credentials.HOME_PAGE_SELECTED_PROJECT)
        assert driver.title == expected_title, get_screenshot(driver, "work_packages", "page_title", expected_title)

    with allure.step('Click "+ Create" green button and select "TASK"'):
        work_packages_page.create_new_task()

    with allure.step('Verify the text "New TASK" on top of the form that got opened on the right side'):
        expected_form_title = Credentials.WORK_PACKAGE_FORM_TITLE
        actual_form_title = work_packages_page.get_work_package_form_title()
        assert actual_form_title == expected_form_title, get_screenshot(driver, "work_packages", "form_title", expected_form_title, actual_form_title)

    with allure.step('Check if webpage title is correct'):
        expected_title = Credentials.NEW_WORK_PACKAGE_PAGE_TITLE.format(Credentials.HOME_PAGE_SELECTED_PROJECT)
        assert driver.title == expected_title, get_screenshot(driver, "work_packages", "page_title", expected_title)

    with allure.step('Fill in task subject and description'):
        work_packages_page.set_task_subject(Credentials.NEW_TASK_SUBJECT)
        work_packages_page.set_task_description(Credentials.NEW_TASK_DESCRIPTION)

    with allure.step('Click "Save" button'):
        work_packages_page.save_new_task()

    with allure.step('Check if webpage title is correct'):
        last_row_data = work_packages_page.get_last_table_row()
        expected_title = Credentials.CREATED_TASK_PAGE_TITLE.format(last_row_data["subject"], last_row_data["id"], Credentials.HOME_PAGE_SELECTED_PROJECT)
        assert driver.title == expected_title, get_screenshot(driver, "work_packages", "page_title", expected_title)

    with allure.step('Verify that a new row was added to the work packages table'):
        current_row_count = work_packages_page.count_table_rows()
        assert initial_row_count + 1 == current_row_count, get_screenshot(driver, "work_packages", "row_count", initial_row_count, current_row_count)

    with allure.step('Verify the subject and type of the last table row'):
        assert Credentials.NEW_TASK_SUBJECT == last_row_data["subject"], get_screenshot(driver, "work_packages", "task_subject", Credentials.NEW_TASK_SUBJECT, last_row_data["subject"])
        assert Credentials.NEW_TASK_TYPE == last_row_data["type"], get_screenshot(driver, "work_packages", "task_type", Credentials.NEW_TASK_TYPE, last_row_data["type"])
