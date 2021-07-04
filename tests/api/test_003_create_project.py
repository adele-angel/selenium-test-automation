"""
Test 003 - API - Create Project

Step:
    Send a request to create a new project with a unique name

Expected Result:
    1. Response status: 201
    2. Response contains a "project" object with name and identifier matching the values set in the request
"""

from config.api import API
from framework.api.projects_api import ProjectsApi


def test_003_create_project():
    data = {
        "name": API.TEST_003["PROJECT_NAME"]
    }

    # Send POST request
    actual = ProjectsApi(API.BASE_URL, API.API_KEY).create_project(data)
    # Parse response to json format
    actual_data = actual.json()

    # Validate status code
    assert actual.status_code == 201, "Failed to get correct response code"
    # Validate project name
    assert actual_data["name"] == API.TEST_003["PROJECT_NAME"], "Failed to get correct project name"
    # Validate project identifier
    assert actual_data["identifier"] == API.TEST_003["PROJECT_IDENTIFIER"], "Failed to get correct project identifier"
