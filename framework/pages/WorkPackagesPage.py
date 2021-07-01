from config.locators import Locators
from infra.web_driver_extensions import WebDriverExtensions
from selenium.webdriver.common.by import By


class WorkPackagesPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver_extended = WebDriverExtensions(driver)

    def create_new_task(self):
        # Click "+" button
        self.driver_extended.get_element((By.XPATH, Locators.dd_actions_xpath)).click()
        # Choose work package of type "Task"
        self.driver_extended.get_visible_element((By.XPATH, Locators.dd_create_task_xpath)).click()

    def set_task_subject(self, task_subject):
        self.driver_extended.get_element((By.XPATH, Locators.input_task_subject_xpath)).send_keys(task_subject)

    def set_task_description(self, task_desc):
        self.driver_extended.get_element((By.XPATH, Locators.editor_task_desc_xpath)).send_keys(task_desc)

    def save_new_task(self):
        self.driver_extended.get_element((By.ID, Locators.btn_save_task_id)).click()

    def count_table_rows(self):
        rows = self.driver_extended.get_elements((By.XPATH, Locators.tb_work_packages_xpath))
        return len(rows)

    def get_last_table_row(self):
        last_row = self.driver_extended.get_element((By.XPATH, Locators.tr_last_work_package_xpath))
        last_row_data = {
            "subject": last_row[3].text,
            "type": last_row[4].text
        }
        return last_row_data

    def click_go_back_button(self):
        self.driver_extended.get_element(Locators.btn_back_xpath).click()
