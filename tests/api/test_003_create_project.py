"""
Test 003 - API - Create Project

Step:
    Send a request to create a new project with a unique name

Expected Result:
    1. Response status: 200
    2. Response contains a "project" object with name and identifier matching the values set in the request
"""

from config.api import TestAPI
from framework.api.projects_api import ProjectsApi


def test_003_create_project():
    data = {
        "name": "Test Project2"
    }

    actual = ProjectsApi(TestAPI.BASE_URL, TestAPI.API_KEY).create_project(data)
    actual_data = actual.json()

    assert actual.status_code == 201, "Failed to get correct response code"
    assert actual_data["name"] == "Test Project2", "Failed to get correct project name"
    assert actual_data["identifier"] == "test-project2", "Failed to get correct project identifier"
