"""
Test 009 - UI - Create Project

Steps:
    1. Login to OpenProject
    2. On "Home" page, click "+ Project" green button
    3. On the "New project" page, type a unique value for the project name. The name should contains letters (upper & lower case), numbers, spaces and some special characters (,/#@$%)
    4. Click "ADVANCED SETTINGS" title
    5. Type some text to the description text box
    6. Verify the value of the "Identifier" field
    7. Select status "On track"
    8. Click "Create"
    9. On "Work packages" page, top left corner: verify the text on the button
"""


from config.credentials import Credentials
from framework.pages.HomePage import HomePage
from framework.pages.NewProjectPage import NewProjectPage
from infra.shared_steps import SharedSteps


def test_009_create_project(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    # Login to OpenProject
    SharedSteps.login_steps(driver)

    # On "Home" page
    home_page = HomePage(driver)
    # Click "+ Project" green button
    home_page.click_new_project()

    # On the "New project" page
    new_project_page = NewProjectPage(driver)
    # type a unique value for the project name
    new_project_page.set_project_name(Credentials.NEW_PROJECT_NAME)
    # Click "ADVANCED SETTINGS" title
    new_project_page.click_advanced_settings()
    # Type some text to the description text box
    new_project_page.set_project_description(Credentials.NEW_PROJECT_DESCRIPTION)
    # Select status "On track"
    new_project_page.set_status(Credentials.NEW_PROJECT_STATUS)

    # Click "Create" and save the project
    new_project_page.save_new_project()

    # TODO: Do ASSERT On "Work packages" page, top left corner: verify the text on the button
    # TODO: Do ASSERT - Button text matches the project name entered in step 3

