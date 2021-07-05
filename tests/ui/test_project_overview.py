import pytest
import allure
from config.credentials import Credentials
from framework.pages.ProjectOverviewPage import ProjectOverviewPage
from infra.shared_steps import SharedSteps


@allure.title('Test navigation into "Project Overview" page')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
def test_verify_project_name(setup):
    with allure.step('setup driver'):
        driver = setup
        driver.get(Credentials.BASE_URL)

    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    with allure.step('Navigate to "Overview" page after selecting a project'):
        SharedSteps.select_project_steps(driver)

    with allure.step("Check if webpage title is correct"):
        assert driver.title == Credentials.PROJECT_OVERVIEW_PAGE_TITLE


@allure.title('Test for matching project name')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
def test_verify_project_name(setup):
    with allure.step('setup driver'):
        driver = setup
        driver.get(Credentials.BASE_URL)

    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    with allure.step('Create a ProjectOverviewPage instance'):
        project_overview_page = ProjectOverviewPage(driver)

    with allure.step("Check if webpage title is correct"):
        assert project_overview_page.get_project_name_from_button() == Credentials.HOME_PAGE_SELECTED_PROJECT
