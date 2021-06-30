"""
Test 002 - API - Update Project

Prerequisites:
    A project named "TestProject1" already exists

Step:
    Send a request to update a project by ID.
    Use a unique string to set as the new project description

Expected Result:
    1. Response status: 200
    2. Response contains a "project" object with description matching the value set in the request
"""

from config.api import API
from framework.api.projects_api import ProjectsApi


def test_002_update_project():
    data = {
        "description": {
            "raw": API.TEST_002["PROJECT_DESC_UPD"]
        }
    }

    # Send PATCH request
    actual = ProjectsApi(API.BASE_URL, API.API_KEY).update_project(API.TEST_001["PROJECT_ID"], data)
    # Parse response to json format
    actual_data = actual.json()

    # Validate status code
    assert actual.status_code == 200, f'Failed to send status code {actual.status_code}'
    # Validate project name
    assert actual_data["name"] == API.TEST_001[
        "PROJECT_NAME"], f'Failed to get matching project name {actual_data["name"]}'
    # Validate project description
    assert actual_data["description"]["raw"] == API.TEST_002[
        "PROJECT_DESC_UPD"], f'Failed to get matching project description {actual_data["description"]["raw"]}'
