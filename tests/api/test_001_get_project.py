"""
Test 001 - API - Get Project by ID

Prerequisites:
    A project named "TestProject1" with description "This is the first test project" already exists

Step:
    Send a request to get a project by ID.
    Use the ID of "TestProject1"

Expected Result:
    1. Response status: 200
    2. Project name is "TestProject1"
    3. Project description is "This is the first test project"
"""

import pytest
import allure
from config.api import API
from framework.api.projects_api import ProjectsApi


@allure.title('Test 001 - API - Get Project by ID')
@pytest.mark.t001
def test_001_get_project():
    # Send GET request
    actual = ProjectsApi(API.BASE_URL, API.API_KEY).get_project(API.TEST_001["PROJECT_ID"])
    # Parse response to json format
    actual_data = actual.json()

    # Validate status code
    assert actual.status_code == 200, f'Failed to send status code: {actual.status_code}'
    # Validate project name
    assert actual_data["name"] == API.TEST_001["PROJECT_NAME"], f'Failed to get matching project name: {actual_data["name"]}'
    # Validate project description
    assert actual_data["description"]["raw"] == API.TEST_001["PROJECT_DESC"], f'Failed to get matching project description: {actual_data["description"]["raw"]}'
