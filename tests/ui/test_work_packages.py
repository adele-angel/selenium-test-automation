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
    initial_row_count = work_packages_page.count_table_rows()

    work_packages_page.create_new_task()
    # Enter task details & save the task
    work_packages_page.set_task_subject(Credentials.NEW_TASK_SUBJECT)
    work_packages_page.set_task_description(Credentials.NEW_TASK_DESCRIPTION)
    work_packages_page.save_new_task()
    # Go back to work packages table and count the rows
    work_packages_page.click_go_back_button()
    new_value = work_packages_page.count_table_rows()

    assert initial_row_count + 1 == new_value
    assert Credentials.NEW_TASK_SUBJECT == work_packages_page.get_last_table_row()["subject"]
    assert Credentials.NEW_TASK_TYPE == work_packages_page.get_last_table_row()["type"]
