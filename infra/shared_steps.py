from config.credentials import Credentials
from framework.pages.LoginPage import LoginPage
from framework.pages.HomePage import HomePage
from framework.pages.ProjectOverviewPage import ProjectOverviewPage


class SharedSteps:

    @staticmethod
    def login_steps(driver):
        login_page = LoginPage(driver)
        login_page.open_login_menu()
        login_page.set_username(Credentials.USERNAME)
        login_page.set_password(Credentials.PASSWORD)
        login_page.click_login()

    @staticmethod
    def select_project_steps(driver):
        home_page = HomePage(driver)
        home_page.select_project(Credentials.HOME_PAGE_SELECTED_PROJECT)

    @staticmethod
    def goto_work_packages_steps(driver):
        project_overview_page = ProjectOverviewPage(driver)
        project_overview_page.click_work_packages()
