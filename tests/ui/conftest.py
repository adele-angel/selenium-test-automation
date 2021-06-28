from selenium import webdriver
import pytest

from config.settings import TestSettings
from utils.webdriver_factory import WebDriverFactory


@pytest.fixture(scope="function")
def setup():
    driver = WebDriverFactory.create_driver("")
    yield driver
    driver.quit()


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
