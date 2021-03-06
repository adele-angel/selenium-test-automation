"""
Test 004 - API - Delete Project

Steps:
    1. Send a request to create a new project with a unique name
        Expected Result:
            1. Response status: 201
            2. Response contains a "project" object with name and identifier matching the value set in the request

    2. Delete the newly created project. Send a request to delete a project by ID
        Expected Result:
            1. Response status: 204

    3. Verify the project was deleted by sending a request to get a project by ID
        Expected Result:
            1. Response status: 404
            2. Response contains an error message: "The requested resource could not be found."
"""

from time import sleep
import pytest
import allure
from config.api import API
from framework.api.projects_api import ProjectsApi


@allure.title('Test 004 - API - Delete Project')
@pytest.mark.t004
def test_004_delete_project():
    data = {
        "name": API.TEST_004["PROJECT_NAME"]
    }

    # Create a new project
    # Send POST request
    actual = ProjectsApi(API.BASE_URL, API.API_KEY).create_project(data)
    actual_data = actual.json()
    project_id = actual_data["id"]
    # Validate status code
    assert actual.status_code == 201, f'Failed to send status code: {actual.status_code}'

    # Delete newly created project
    # Send DELETE request
    delete_action = ProjectsApi(API.BASE_URL, API.API_KEY).delete_project(project_id)
    # Validate status code
    assert delete_action.status_code == 204, f'Failed to send status code: {actual.status_code}'

    # Confirm the project was deleted
    sleep(5)  # wait for actual server side delete
    # Send GET request
    get_action = ProjectsApi(API.BASE_URL, API.API_KEY).get_project(project_id)
    # Validate status code
    assert get_action.status_code == 404, f'Failed to send status code: {actual.status_code}'
