from config.credentials import Credentials
from framework.pages.HomePage import HomePage
from infra.shared_steps import SharedSteps


def test_click_new_project(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    SharedSteps.login_steps(driver)

    home_page = HomePage(driver)
    home_page.click_new_project()

    assert driver.title == Credentials.NEW_PROJECT_PAGE_TITLE


def test_select_project(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    SharedSteps.login_steps(driver)
    SharedSteps.select_project_steps(driver)

    assert Credentials.HOME_PAGE_SELECTED_PROJECT.lower() in driver.current_url
    assert f'title="{Credentials.HOME_PAGE_SELECTED_PROJECT}"' in driver.page_source
