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

import pytest
import allure
from config.credentials import Credentials
from framework.pages.HomePage import HomePage
from framework.pages.NewProjectPage import NewProjectPage
from infra.shared_steps import SharedSteps


@allure.title("Test Creating A New Project")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.project
def test_009_create_project(setup):
    with allure.step("setup driver"):
        driver = setup
        driver.get(Credentials.BASE_URL)

    # step 1
    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    # step 2
    with allure.step('On "Home" page, click "+ Project" green button'):
        home_page = HomePage(driver)
        home_page.click_new_project_button()

    # step 3
    with allure.step('On the "New project" page, type a unique value for the project name'):
        new_project_page = NewProjectPage(driver)
        new_project_page.set_project_name(Credentials.NEW_PROJECT_NAME)

    # step 4
    with allure.step('Click "ADVANCED SETTINGS" title'):
        new_project_page.click_advanced_settings()

    # step 5
    with allure.step('Type some text to the description text box'):
        new_project_page.set_project_description(Credentials.NEW_PROJECT_DESCRIPTION)

    # step 6
    with allure.step('Verify the value of the "Identifier" field'):
        pass

    # step 7
    with allure.step('Select status "On track"'):
        new_project_page.set_status(Credentials.NEW_PROJECT_STATUS)

    # step 8
    with allure.step('Click "Create" and save the project'):
        new_project_page.save_new_project()

    # step 9
    with allure.step('On "Work packages" page, top left corner: verify the text on the button'):
        pass

    # TODO: Do ASSERT On "Work packages" page, top left corner: verify the text on the button
    # TODO: Do ASSERT - Button text matches the project name entered in step 3
