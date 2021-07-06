import pytest
import allure
from config.credentials import Credentials
from framework.pages.ProjectOverviewPage import ProjectOverviewPage
from framework.pages.NewProjectPage import NewProjectPage
from infra.shared_steps import SharedSteps
from infra.string_util import identifier_generator, clean_spaces


@allure.title('Test navigation into "New Project" page')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.sanity
@pytest.mark.new_project
@pytest.mark.project
def test_new_project_page_title(setup):
    with allure.step('Setup driver'):
        driver = setup
        driver.get(Credentials.BASE_URL)

    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    with allure.step('On "Home" page, click "+ Project" green button'):
        SharedSteps.click_create_new_project_steps(driver)

    with allure.step("Check if webpage title is correct"):
        assert driver.title == Credentials.NEW_PROJECT_PAGE_TITLE


@allure.title('Test creating a new project')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.sanity
@pytest.mark.new_project
@pytest.mark.project
def test_create_new_project(setup):
    with allure.step('Setup driver'):
        driver = setup
        driver.get(Credentials.BASE_URL)

    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    with allure.step('On "Home" page, click "+ Project" green button'):
        SharedSteps.click_create_new_project_steps(driver)

    with allure.step('Enter project info'):
        with allure.step('Create a NewProjectPage instance'):
            new_project_page = NewProjectPage(driver)
        with allure.step('Type project name'):
            new_project_page.set_project_name(Credentials.NEW_PROJECT_NAME)
        with allure.step('Click "ADVANCED SETTINGS" title'):
            new_project_page.click_advanced_settings()
            with allure.step('Type project description'):
                new_project_page.set_project_description(Credentials.NEW_PROJECT_DESCRIPTION)
            with allure.step('Select project status'):
                new_project_page.set_status(Credentials.NEW_PROJECT_STATUS)

    with allure.step('Save project'):
        new_project_page.save_new_project()

    with allure.step('Create a ProjectOverviewPage instance'):
        project_overview_page = ProjectOverviewPage(driver)
    with allure.step('On "Work packages" page, top left corner: verify the text on the button'):
        assert project_overview_page.get_project_name_from_button() == clean_spaces(Credentials.NEW_PROJECT_NAME)

    with allure.step('Verify the value of the "identifier" field'):
        # Note 1: can't verify project's identifier before saving the new project (original step 6)
        # Note 2: OpenProject's identifier field doesn't match project requirements for special characters
        assert identifier_generator(Credentials.NEW_PROJECT_NAME) in driver.current_url
