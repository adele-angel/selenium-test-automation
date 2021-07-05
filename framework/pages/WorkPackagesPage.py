from config.locators import Locators
from infra.web_driver_extensions import WebDriverExtensions
from selenium.webdriver.common.by import By


class WorkPackagesPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver_extended = WebDriverExtensions(driver)

    def create_new_task(self):
        # Click "+ Create" button
        self.driver_extended.get_element((By.CLASS_NAME, Locators.dd_create_work_package_class)).click()
        # Choose work package of type "Task"
        self.driver_extended.get_visible_element((By.XPATH, Locators.dd_create_task_xpath)).click()
        self.driver_extended.until_visible((By.CLASS_NAME, Locators.form_new_task_class))

    def get_work_package_form_title(self):
        work_package_status = self.driver_extended.get_element((By.CLASS_NAME, Locators.edit_work_package_status_class)).text
        work_package_type = self.driver_extended.get_element((By.CLASS_NAME, Locators.edit_work_package_type_class)).text
        return f"{work_package_status} {work_package_type}"

    def set_task_subject(self, task_subject):
        self.driver_extended.get_visible_element((By.XPATH, Locators.input_task_subject_xpath)).send_keys(task_subject)

    def set_task_description(self, task_desc):
        self.driver_extended.get_element((By.XPATH, Locators.editor_task_desc_xpath)).send_keys(task_desc)

    def save_new_task(self):
        self.driver_extended.get_element((By.ID, Locators.btn_save_task_id)).click()
        self.driver_extended.until_not_exists_or_hidden((By.ID, Locators.btn_save_task_id))

    def count_table_rows(self):
        rows = self.driver_extended.get_elements((By.XPATH, Locators.tb_work_packages_xpath))
        return len(rows)

    def get_last_table_row(self):
        last_row = self.driver_extended.get_elements((By.XPATH, Locators.tr_last_work_package_xpath))
        return {
            "id": last_row[0].find_element_by_tag_name("a").text,
            "subject": last_row[3].text,
            "type": last_row[4].text
        }

    def click_go_back_button(self):
        self.driver_extended.get_enabled_element((By.CLASS_NAME, Locators.btn_back_class)).click()
