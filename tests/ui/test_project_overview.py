from config.credentials import Credentials
from framework.pages.ProjectOverviewPage import ProjectOverviewPage
from infra.shared_steps import SharedSteps


def test_verify_project_name(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    SharedSteps.login_steps(driver)

    project_overview_page = ProjectOverviewPage(driver)
    # TODO: is this test necessary? what tests to add?
    assert project_overview_page.get_project_name_from_menu() == Credentials.HOME_PAGE_SELECTED_PROJECT
