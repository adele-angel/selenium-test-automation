import time

from config.credentials import Credentials
from framework.pages.WorkPackagesPage import WorkPackagesPage
from infra.shared_steps import SharedSteps


def test_create_new_task(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    # Login to app
    SharedSteps.login_steps(driver)
    # Go to selected project overview and choose "work packages"
    SharedSteps.select_project_steps(driver)
    SharedSteps.goto_work_packages_steps(driver)

    work_packages_page = WorkPackagesPage(driver)
    # TODO: change to time.sleep() function into a waiter
    time.sleep(1)
    initial_row_count = work_packages_page.get_table_row_count()

    work_packages_page.create_new_task()
    # TODO: change to time.sleep() function into a waiter
    time.sleep(1)
    work_packages_page.set_task_subject(Credentials.NEW_TASK_SUBJECT)
    work_packages_page.set_task_description(Credentials.NEW_TASK_DESCRIPTION)

    work_packages_page.save_new_task()
    # TODO: change to time.sleep() function into a waiter
    time.sleep(5)
    work_packages_page.click_go_back_button()
    # TODO: change to time.sleep() function into a waiter
    time.sleep(1)

    assert initial_row_count + 1 == work_packages_page.get_table_row_count()
    assert Credentials.NEW_TASK_SUBJECT == work_packages_page.get_last_table_row()["subject"]
