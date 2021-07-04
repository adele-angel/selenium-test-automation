from selenium import webdriver
from config.settings import Settings


class WebDriverFactory:
    @staticmethod
    def create_driver(driver_name):
        if driver_name == "chrome":
            driver = webdriver.Chrome(executable_path=Settings.CHROME_EXECUTABLE_PATH)
        elif driver_name == "firefox":
            driver = webdriver.Firefox(executable_path=Settings.FIREFOX_EXECUTABLE_PATH)
        else:  # Default browser is Chrome
            driver = webdriver.Chrome(executable_path=Settings.CHROME_EXECUTABLE_PATH)
        return driver
