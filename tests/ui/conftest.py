import pytest
from config.settings import Settings
from infra.webdriver_factory import WebDriverFactory


# TODO: configure browser selection
@pytest.fixture(scope="function")
def setup():
    driver = WebDriverFactory.create_driver("chrome")
    # if browser.param == "chrome":
    #     driver = WebDriverFactory.create_driver("chrome")
    # elif browser.param == "firefox":
    #     driver = WebDriverFactory.create_driver("firefox")
    # else:  # Default browser is Chrome
    #     driver = WebDriverFactory.create_driver("chrome")
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=Settings.DEFAULT_BROWSER)
    parser.addoption("--env", action="store", default=Settings.ENV)


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):  # hook for Adding Environment info to HTML Report
    config._metadata["Project Name"] = "Selenium Test Automation"
    config._metadata["Environment"] = Settings.ENV
    config._metadata["Tester"] = "Adele Angel"
    config._metadata["Package"] = "python 3.9.5"


@pytest.mark.parametrize  # hook for delete/modify environment info to HTML Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
