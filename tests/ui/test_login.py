import pytest
import allure
from config.credentials import Credentials
from framework.pages.LoginPage import LoginPage


@allure.title('Test OpenProject sign in page title')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.sanity
@pytest.mark.login
def test_login_page_title(setup):
    with allure.step('Setup driver'):
        driver = setup
        driver.get(Credentials.BASE_URL)

    with allure.step('Check if webpage title is correct'):
        assert driver.title == Credentials.LOGIN_PAGE_TITLE


@allure.title('Test logging into OpenProject app')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.sanity
@pytest.mark.login
def test_login(setup):
    with allure.step('Setup driver'):
        driver = setup
        driver.get(Credentials.BASE_URL)

    with allure.step('Create a loginPage instance'):
        login_page = LoginPage(driver)

    with allure.step('Opening "Sign in" menu'):
        login_page.open_login_menu()

    with allure.step('Entering username and password'):
        login_page.set_username(Credentials.USERNAME)
        login_page.set_password(Credentials.PASSWORD)

    with allure.step('Clicking "Sign in" button'):
        login_page.click_login()

    with allure.step('Validating login by checking if sign out action exists'):
        assert login_page.can_sign_out()
