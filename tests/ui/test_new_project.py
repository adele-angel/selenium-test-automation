from config.credentials import Credentials
from framework.pages.HomePage import HomePage
from infra.data_generator import DataGenerator
from infra.shared_steps import SharedSteps
from framework.pages.NewProjectPage import NewProjectPage


def test_create_new_project(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    SharedSteps.login_steps(driver)
    SharedSteps.click_create_new_project_steps(driver)

    new_project_page = NewProjectPage(driver)
    # Enter project details
    new_project_page.set_project_name(Credentials.NEW_PROJECT_NAME)
    new_project_page.click_advanced_settings()
    new_project_page.set_project_description(Credentials.NEW_PROJECT_DESCRIPTION)
    new_project_page.set_status(Credentials.NEW_PROJECT_STATUS)
    # Save project
    new_project_page.save_new_project()

    actual_identifier = new_project_page.get_project_identifier()
    print(actual_identifier)

    # TODO: Add asserts
    assert DataGenerator.identifier_generator(Credentials.NEW_PROJECT_NAME) == actual_identifier
