import pytest
from selenium import webdriver

from config.settings import TestSettings


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=TestSettings.CHROME_EXECUTABLE_PATH)
        print("Launching Chrome Browser...")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=TestSettings.FIREFOX_EXECUTABLE_PATH)
        print("Launching Firefox Browser...")
    else:
        driver = webdriver.Chrome(executable_path=TestSettings.CHROME_EXECUTABLE_PATH)
        print("Launching Chrome Browser...")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = "Selenium Automation Project"
    config._metadata['Tester'] = "Adele Angel"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
