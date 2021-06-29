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


from config.api import TestAPI
from framework.api.projects_api import ProjectsApi


def test_002_update_project():
    data = {
        "description": {
            "raw": TestAPI.PROJECT_DESC_UPD
        }
    }
    actual = ProjectsApi(TestAPI.BASE_URL, TestAPI.API_KEY).update_project("5", data)
    actual_data = actual.json()

    assert actual.status_code == 200, "Failed to get correct response code"
    assert actual_data["name"] == TestAPI.PROJECT_TITLE, "Failed to get correct project name"
    assert actual_data["description"]["raw"] == TestAPI.PROJECT_DESC_UPD, "Failed to get correct project description"
