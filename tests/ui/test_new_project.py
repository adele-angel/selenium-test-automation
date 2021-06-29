from framework.pages import HomePage
from framework.pages.NewProjectPage import NewProjectPage
from config.credentials import Credentials
from infra.shared_steps import SharedSteps


def test_create_new_project(setup):
    driver = setup
    driver.get(Credentials.BASE_URL)

    SharedSteps.login_steps(driver)

    home_page = HomePage(driver)
    home_page.click_new_project()

    new_project_page = NewProjectPage(driver)
    new_project_page.set_project_name(Credentials.NEW_PROJECT_NAME)
    new_project_page.click_advanced_settings()
    new_project_page.set_project_description(Credentials.NEW_PROJECT_DESCRIPTION)
    new_project_page.set_status(Credentials.NEW_PROJECT_STATUS)
    new_project_page.save_new_project()

    msg = driver.find_element_by_tag_name("body").text
    print(msg)

    #
    # print(project_name)
    #
    # if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)” + “(?=.*[-+_!@#$%^&*., ?]).+$", project_name):
    #     logger.info("**** Project name test passed ****")
    #     driver.close()
    #     assert True
    # else:
    #     logger.error("**** Project name test test failed ****")
    #     driver.save_screenshot(TestSettings.SCREENSHOT_PATH + "009_004_new_project_page_create.png")
    #     driver.close()
    #     assert False
