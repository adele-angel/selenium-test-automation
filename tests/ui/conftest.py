from selenium import webdriver
import pytest

from config.settings import TestSettings


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path=TestSettings.CHROME_EXECUTABLE_PATH)
    print("Launching Chrome browser...")
    return driver


"""
PyTest HTML Report
"""


def pytest_configure(config):  # hook for Adding Environment info to HTML Report
    config._metadata['Project Name'] = 'Selenium Test Automation'
    config._metadata['Tester'] = 'Adele Angel'
    config._metadata['Package'] = 'python 3.9.5'


@pytest.mark.parametrize  # hook for delete/modify environment info to HTML Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
