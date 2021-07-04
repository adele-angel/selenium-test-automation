import allure
import pytest
from config.credentials import Credentials
from framework.pages.HomePage import HomePage
from infra.shared_steps import SharedSteps


@allure.title('Test navigation into "New Project" Page')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_click_new_project(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    with allure.step('On "Home" page, click "+ Project" green button'):
        home_page = HomePage(driver)
        home_page.click_new_project_button()

    with allure.step('Verify navigation into "New Project" page'):
        assert driver.title == Credentials.NEW_PROJECT_PAGE_TITLE


@allure.title('Test navigation into a selected project page')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_select_project(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    with allure.step('Click "Select a project" menu button, and select a project from the drop-down'):
        home_page = HomePage(driver)
        home_page.select_project(Credentials.HOME_PAGE_SELECTED_PROJECT)

    with allure.step('Verify the value of the "identifier" field'):
        assert Credentials.HOME_PAGE_SELECTED_PROJECT.lower() in driver.current_url
        assert f'title="{Credentials.HOME_PAGE_SELECTED_PROJECT}"' in driver.page_source
