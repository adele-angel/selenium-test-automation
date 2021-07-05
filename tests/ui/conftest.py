import pytest
from config.settings import Settings
from infra.webdriver_factory import WebDriverFactory


@pytest.fixture(scope="function")
def setup(browser):
    # Create a driver
    driver = WebDriverFactory.create_driver(browser)
    # Return the driver object by the end of the setup
    yield driver
    # For cleanup, quit the driver instance
    driver.quit()


def pytest_addoption(parser):
    # Setting default browser
    parser.addoption("--browser", action="store", default=Settings.DEFAULT_BROWSER)
    # Setting default environment
    parser.addoption("--env", action="store", default=Settings.ENV)


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):  # Hook for Adding Environment info to HTML Report
    config._metadata["Project Name"] = "Selenium Test Automation"
    config._metadata["Environment"] = Settings.ENV
    config._metadata["Tester"] = "Adele Angel"
    config._metadata["Package"] = "python 3.9.5"


@pytest.mark.parametrize  # Hook for delete/modify environment info to HTML Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
