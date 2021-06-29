"""
Test 001 - API - Get Project by ID

Prerequisites:
    A project named "TestProject1" with description "This is the first test project" already exists

Step:
    Send a request to get a project by ID. Use the ID of "TestProject1"

Expected Result:
    1. Response status: 200
    2. Project name is "TestProject1"
    3. Project description is "This is the first test project"
"""

from config.api import TestAPI
from framework.api.projects_api import ProjectsApi


def test_001_get_project():
    actual = ProjectsApi(TestAPI.BASE_URL, TestAPI.API_KEY).get_project("1")
    actual_data = actual.json()

    assert actual.status_code == 200, f'Failed to send status code {actual.status_code}'
    assert actual_data["name"] == TestAPI.PROJECT_TITLE, "Failed to get correct project name"
    assert actual_data["description"]["raw"] == TestAPI.PROJECT_DESC, "Failed to get correct project description " + \
                                                                      actual_data["description"]["raw"]
