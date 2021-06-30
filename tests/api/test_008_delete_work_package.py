"""
Test 008 - API - Delete Work Package

Step:
    1. Send a request to create a new work package with a unique name
        Expected Result:
            1. Response status: 201
            2. Response contains a "work package" object with subject matching the value set in the request

    2. Delete the newly created work package. Send a request to delete a work package by ID
        Expected Result:
            1. Response status: 204

    3. Verify the work package was deleted by sending a request to get a work package by ID
        Expected Result:
            1. Response status: 404
            2. Response contains an error "message": "The requested resource could not be found."
"""

from time import sleep
from config.api import API
from framework.api.work_packages_api import WorkPackagesApi


def test_008_delete_work_package():
    data = {
        "subject": API.TEST_008["WORK_PACKAGE_SUBJECT"],
        "_links": {
            "project": {
                "href": f'/api/v3/projects/{API.TEST_001["PROJECT_ID"]}'
            }
        }
    }

    # Create a new work package
    # Send POST request
    actual = WorkPackagesApi(API.BASE_URL, API.API_KEY).create_work_package(data)
    actual_data = actual.json()
    work_package_id = actual_data["id"]
    assert actual.status_code == 201, f'Failed to get correct response code {actual.status_code}'

    # Delete newly created work package
    # Send DELETE request
    delete_action = WorkPackagesApi(API.BASE_URL, API.API_KEY).delete_work_package(work_package_id)
    assert delete_action.status_code == 204, f'Failed to get correct response code {delete_action.status_code}'

    # Confirm the work package was deleted
    sleep(5)  # wait for actual server side delete
    # Send GET request
    get_action = WorkPackagesApi(API.BASE_URL, API.API_KEY).get_work_package(work_package_id)
    assert get_action.status_code == 404, f'Failed to get correct response code {get_action.status_code}'
