from config.credentials import Credentials
from framework.pages.HomePage import HomePage
from infra.shared_steps import SharedSteps


def test_click_new_project(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    # Do login
    SharedSteps.login_steps(driver)

    home_page = HomePage(driver)
    home_page.click_new_project_button()

    assert driver.title == Credentials.NEW_PROJECT_PAGE_TITLE


def test_select_project(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    # Do login
    SharedSteps.login_steps(driver)

    home_page = HomePage(driver)
    home_page.select_project(Credentials.HOME_PAGE_SELECTED_PROJECT)

    assert Credentials.HOME_PAGE_SELECTED_PROJECT.lower() in driver.current_url
    assert f'title="{Credentials.HOME_PAGE_SELECTED_PROJECT}"' in driver.page_source
