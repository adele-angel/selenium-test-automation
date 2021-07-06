# selenium-test-automation [![python version: 3.9.6](https://img.shields.io/badge/python%20version-3.9.6-blue)](https://python.org/) [![pip version: 21.1.3](https://img.shields.io/badge/pip%20version-21.1.3-blue)](https://pypi.org/project/pip/) [![allure version: 2.14.0](https://img.shields.io/badge/allure%20version-2.14.0-blue)](https://docs.qameta.io/allure/)

Test Automation Project for "OpenProject" Software

## API Automation

Official OpenProject API documentation here: https://docs.openproject.org/api

### General Guidelines for API Tests Automation

1. Using Postman to experiment with the various API calls manually.
2. Manually validate that expected result can be seen in the UI.
3. Implementation of the API requests using Python and the Requests library.
4. Creating a dedicated configuration file.

## UI Automation

### General Guidelines for UI Tests Automation

1. Using Selenium WebDriver for browser automation.
2. Automation implementation using the "Page Object Model" design pattern.
3. Using assertions to implement validations for each expected result specified in the test cases below.

## Generate Allure Reports

```
$ pytest --alluredir={results dir} {test dir}

Run on server
$ allure serve {results dir}

Create static files
$ allure generate {results dir}
```

## Packages

[![selenium version: 3.141.0](https://img.shields.io/badge/selenium%20version-3.141.0-green)](https://pypi.org/project/selenium/)
[![pytest version: 6.2.4](https://img.shields.io/badge/pytest%20version-6.2.4-green)](https://pypi.org/project/pytest/)
[![allure-pytest version: 2.9.43](https://img.shields.io/badge/allure--pytest%20version-2.9.43-green)](https://pypi.org/project/allure-pytest/)
[![requests version: 2.25.1](https://img.shields.io/badge/requests%20version-2.25.1-green)](https://pypi.org/project/requests/)

```
$ pip install selenium pytest requests allure-pytest
```

## Project Setup

Installation of OpenProject using Docker To install OpenProject locally on your machine, please follow the instructions here:
https://docs.openproject.org/installation-and-operations/installation/docker/
