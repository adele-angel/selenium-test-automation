from config.credentials import Credentials
from framework.pages.LoginPage import LoginPage


def test_login_page_title(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    assert driver.title == Credentials.LOGIN_PAGE_TITLE


def test_login(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    login_page = LoginPage(driver)
    login_page.open_login_menu()
    login_page.set_username(Credentials.USERNAME)
    login_page.set_password(Credentials.PASSWORD)
    login_page.click_login()

    assert driver.title == Credentials.HOME_PAGE_TITLE
