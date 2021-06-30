"""
Test 010 - UI - Create Task

Prerequisites:
    A project named "TestProject1" already exists

Steps:
    1. Login to OpenProject
    2. On "Home" page, top-left corner, click "Select a project" menu button, and select "TestProject1" from the drop-down
    3. On the "Project Overview" page, left side menu, click "Work packages". Once on the "Work packages" page, note the number of rows displayed in the work packages table.
    4. Click "+ Create" green button and select "TASK"
    5. Verify the text "New TASK" on top of the form that got opened on the right side
    6. Type unique strings into the subject and description boxes
    7. Click "Save" button
    8. Verify that a new row was added to the work packages table
    9. Verify the subject and type of the last table row
"""

from config.credentials import Credentials
from framework.pages.WorkPackagesPage import WorkPackagesPage
from infra.shared_steps import SharedSteps


def test_009_create_task(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    # Login to OpenProject
    SharedSteps.login_steps(driver)

    # On "Home" page click "Select a project" menu button, and select "TestProject1" from the drop-down
    SharedSteps.select_project_steps(driver)

    # On the "Project Overview" page, left side menu, click "Work packages"
    SharedSteps.goto_work_packages_steps(driver)

    # Note the number of rows displayed in the work packages table
    work_packages_page = WorkPackagesPage(driver)
    initial_row_count = work_packages_page.get_table_row_count()

    # Click "+ Create" green button and select "TASK"

    # Verify the text "New TASK" on top of the form that got opened on the right side
    # TODO: ASSERT The title of the form is "New TASK"

    # Type unique strings into the subject and description boxes
    # Click "Save" button

    # Verify that a new row was added to the work packages table
    # TODO: ASSERT

    # Verify the subject and type of the last table row
    # TODO: ASSERT
