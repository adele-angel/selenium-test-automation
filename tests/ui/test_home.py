import pytest
import allure
from config.credentials import Credentials
from framework.pages.HomePage import HomePage
from infra.shared_steps import SharedSteps
from infra.string_util import identifier_generator


@allure.title('Test navigation into "New Project" page')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.sanity
@pytest.mark.home
@pytest.mark.project
def test_click_create_new_project(setup):
    with allure.step('Setup driver'):
        driver = setup
        driver.get(Credentials.BASE_URL)

    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    with allure.step('Create a HomePage instance'):
        home_page = HomePage(driver)

    with allure.step('On "Home" page, click "+ Project" green button'):
        home_page.click_new_project_button()

    with allure.step('Verify navigation into "New Project" page'):
        assert driver.title == Credentials.NEW_PROJECT_PAGE_TITLE


@allure.title('Test navigation into a selected project page')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.sanity
@pytest.mark.home
@pytest.mark.project
def test_select_project(setup):
    with allure.step('Setup driver'):
        driver = setup
        driver.get(Credentials.BASE_URL)

    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    with allure.step('Create a HomePage instance'):
        home_page = HomePage(driver)

    with allure.step('Click "Select a project" menu button, and select a project from the drop-down'):
        home_page.select_project(Credentials.HOME_PAGE_SELECTED_PROJECT)

    with allure.step('Verify the value of the "identifier" field'):
        # Note: OpenProject's identifier field doesn't match project requirements for special characters
        assert identifier_generator(Credentials.HOME_PAGE_SELECTED_PROJECT) in driver.current_url
        # Another option
        assert f'title="{Credentials.HOME_PAGE_SELECTED_PROJECT}"' in driver.page_source
