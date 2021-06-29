"""
Test 004 - API - Delete Project

Step:
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
            2. Response contains an error "message": "Work packages in non descendant projects reference versions of the project or its descendants."
"""
from time import sleep

from config.api import TestAPI
from framework.api.projects_api import ProjectsApi


def test_004_delete_project():
    # Creating a new project
    data = {
        "name": "TestProject5"
    }

    actual = ProjectsApi(TestAPI.BASE_URL, TestAPI.API_KEY).create_project(data)
    actual_data = actual.json()
    project_id = actual_data["id"]
    assert actual.status_code == 201, project_id

    # Delete newly created project
    delete_action = ProjectsApi(TestAPI.BASE_URL, TestAPI.API_KEY).delete_project(project_id)
    assert delete_action.status_code == 204

    # Confirm project was deleted
    sleep(5)  # wait for actual server side delete
    get_action = ProjectsApi(TestAPI.BASE_URL, TestAPI.API_KEY).get_project(project_id)
    assert get_action.status_code == 404