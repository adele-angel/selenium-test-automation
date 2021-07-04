import pytest
import allure
from config.credentials import Credentials
from framework.pages.LoginPage import LoginPage


@allure.title("Test OpenProject sign in page title")
@allure.severity(allure.severity_level.MINOR)
def test_login_page_title(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    with allure.step("Check if webpage title is correct"):
        assert driver.title == Credentials.LOGIN_PAGE_TITLE


@allure.title("Test logging into OpenProject app")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.test_009
@pytest.mark.test_010
def test_login(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    login_page = LoginPage(driver)

    with allure.step("Opening 'sign in' menu"):
        login_page.open_login_menu()

    with allure.step("Entering username and password"):
        login_page.set_username(Credentials.USERNAME)
        login_page.set_password(Credentials.PASSWORD)

    with allure.step("Clicking 'sign in' button"):
        login_page.click_login()

    with allure.step("Validating login by checking if sign out action exists"):
        assert login_page.can_sign_out()
