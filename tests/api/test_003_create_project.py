"""
Test 003 - API - Create Project

Step:
    Send a request to create a new project with a unique name

Expected Result:
    1. Response status: 201
    2. Response contains a "project" object with name and identifier matching the values set in the request

Important Note:
    OpenProject's identifier field doesn't match project requirements for special characters.
    Using some special characters such as $, ^, \ etc. might result an invalid identifier.
"""

import pytest
import allure
from config.api import API
from framework.api.projects_api import ProjectsApi
from infra.string_util import identifier_generator


@allure.title('Test 003 - API - Create Project')
@pytest.mark.t003
def test_003_create_project():
    data = {
        "name": API.TEST_003["PROJECT_NAME"]
    }

    # Send POST request
    actual = ProjectsApi(API.BASE_URL, API.API_KEY).create_project(data)
    # Parse response to json format
    actual_data = actual.json()

    # Validate status code
    assert actual.status_code == 201, f'Failed to send status code: {actual.status_code}'
    # Validate project name
    assert actual_data["name"] == data["name"], f'Failed to get matching project name: {actual_data["name"]}'
    # Validate project identifier
    assert actual_data["identifier"] == identifier_generator(data["name"]), f'Failed to get matching project identifier: {actual_data["identifier"]}'
