from config.credentials import Credentials
from infra.shared_steps import SharedSteps


def test_login_page_title(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    assert driver.title == Credentials.LOGIN_PAGE_TITLE


def test_login(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    SharedSteps.login_steps(driver)

    assert driver.title == Credentials.HOME_PAGE_TITLE
