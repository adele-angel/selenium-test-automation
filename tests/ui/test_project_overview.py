import pytest
import allure
from config.credentials import Credentials
from framework.pages.ProjectOverviewPage import ProjectOverviewPage
from infra.screenshot_generator import get_screenshot
from infra.shared_steps import SharedSteps
from infra.string_util import clean_spaces


@allure.title('Test navigation into "Project Overview" page')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.sanity
@pytest.mark.overview
def test_project_overview_page_title(setup):
    with allure.step('Setup driver'):
        driver = setup
        driver.get(Credentials.BASE_URL)

    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    with allure.step('Navigate to "Overview" page after selecting a project'):
        SharedSteps.select_project_steps(driver)

    with allure.step("Check if webpage title is correct"):
        assert driver.title == Credentials.PROJECT_OVERVIEW_PAGE_TITLE, get_screenshot(driver, "project_overview", "page_title", Credentials.PROJECT_OVERVIEW_PAGE_TITLE)


@allure.title('Test for matching project name')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.sanity
@pytest.mark.overview
@pytest.mark.project
def test_verify_project_name(setup):
    with allure.step('Setup driver'):
        driver = setup
        driver.get(Credentials.BASE_URL)

    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    with allure.step('Navigate to "Overview" page after selecting a project'):
        SharedSteps.select_project_steps(driver)

    with allure.step('Create a ProjectOverviewPage instance'):
        project_overview_page = ProjectOverviewPage(driver)

    with allure.step('Check if selected proj is correct'):
        expected_project_name = clean_spaces(Credentials.HOME_PAGE_SELECTED_PROJECT)
        actual_project_name = project_overview_page.get_project_name_from_button()
        assert actual_project_name == expected_project_name, get_screenshot(driver, "project_overview", "name", expected_project_name, actual_project_name)
