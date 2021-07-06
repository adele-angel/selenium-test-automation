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
from framework.pages.NewProjectPage import NewProjectPage
from framework.pages.ProjectOverviewPage import ProjectOverviewPage
from infra.screenshot_generator import get_screenshot
from infra.shared_steps import SharedSteps
from infra.string_util import is_unique_str, identifier_generator, clean_spaces


@allure.title('Test 009 - UI - Create Project')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.t009
@pytest.mark.project
def test_009_create_project(setup):
    with allure.step('Setup driver'):
        driver = setup
        driver.get(Credentials.BASE_URL)

    # step 1
    with allure.step('Login to OpenProject'):
        SharedSteps.login_steps(driver)

    # step 2
    with allure.step('On "Home" page, click "+ Project" green button'):
        SharedSteps.click_create_new_project_steps(driver)

    # step 3
    with allure.step('On the "New project" page, type a unique value for the project name'):
        with allure.step('Create a NewProjectPage instance'):
            new_project_page = NewProjectPage(driver)
        with allure.step('Type project name'):
            new_project_page.set_project_name(Credentials.NEW_PROJECT_NAME)

    # step 4
    with allure.step('Click "ADVANCED SETTINGS" title'):
        new_project_page.click_advanced_settings()

    # step 5
    with allure.step('Type some text to the description text box'):
        new_project_page.set_project_description(Credentials.NEW_PROJECT_DESCRIPTION)

    # step 6
    with allure.step('Verify project name is a unique string'):
        # Note: see step 10*
        assert is_unique_str(Credentials.NEW_PROJECT_NAME), get_screenshot(driver, "009", "unique", Credentials.NEW_PROJECT_NAME)

    # step 7
    with allure.step('Select status "On track"'):
        new_project_page.set_status(Credentials.NEW_PROJECT_STATUS)

    # step 8
    with allure.step('Click "Create" and save the project'):
        new_project_page.save_new_project()

    # step 9
    with allure.step('On "Work packages" page, top left corner: verify the text on the button'):
        with allure.step('Create a NewProjectPage instance'):
            project_overview_page = ProjectOverviewPage(driver)
        with allure.step('Verify the text on the button'):
            expected_project_name = clean_spaces(Credentials.NEW_PROJECT_NAME)
            actual_project_name = project_overview_page.get_project_name_from_button()
            assert actual_project_name == expected_project_name, get_screenshot(driver, "009", "name", actual_project_name, expected_project_name)

    # step 10*
    with allure.step('Verify the value of the "Identifier" field'):
        # Note 1: can't verify project's identifier before saving the new project (original step 6)
        # Note 2: OpenProject's identifier field doesn't match project requirements for special characters
        # Two options to verify
        expected_identifier = identifier_generator(Credentials.NEW_PROJECT_NAME)
        assert new_project_page.get_project_identifier() == expected_identifier, get_screenshot(driver, "009", "identifier", expected_identifier, new_project_page.get_project_identifier())
        assert expected_identifier in driver.current_url, get_screenshot(driver, "009", "identifier", expected_identifier)
