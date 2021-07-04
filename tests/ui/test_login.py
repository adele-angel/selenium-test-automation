import pytest
import allure
from config.credentials import Credentials
from framework.pages.LoginPage import LoginPage


@allure.severity(allure.severity_level.MINOR)
def test_login_page_title(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    assert driver.title == Credentials.LOGIN_PAGE_TITLE


@allure.title("Test logging into OpenProject app")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
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
    with allure.step("Check if webpage title is correct"):
        assert driver.title == Credentials.HOME_PAGE_TITLE
