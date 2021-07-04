from time import sleep

import pytest
import allure
from config.credentials import Credentials
from infra.shared_steps import SharedSteps
from framework.pages.NewProjectPage import NewProjectPage


@allure.title("Test creation of a new project")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.test_009
def test_create_new_project(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    SharedSteps.login_steps(driver)
    SharedSteps.click_create_new_project_steps(driver)

    new_project_page = NewProjectPage(driver)

    with allure.step("Enter project info"):
        new_project_page.set_project_name(Credentials.NEW_PROJECT_NAME)
        new_project_page.click_advanced_settings()
        new_project_page.set_project_description(Credentials.NEW_PROJECT_DESCRIPTION)
        new_project_page.set_status(Credentials.NEW_PROJECT_STATUS)

    with allure.step("Save project"):
        new_project_page.save_new_project()

    with allure.step('Verify the value of the "identifier" field'):
        # TODO: maybe add REGEX
        # TODO: change sleeper
        # Note: OpenProject's identifier field doesn't match project requirements for special characters
        sleep(3)
        assert Credentials.NEW_PROJECT_IDENTIFIER in driver.current_url

    with allure.step('On "Work packages" page, top left corner: verify the text on the button'):
        assert new_project_page.get_project_name_from_button(Credentials.NEW_PROJECT_NAME) == Credentials.NEW_PROJECT_NAME
