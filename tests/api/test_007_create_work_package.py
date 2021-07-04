"""
Test 007 - API - Create Work Package

Prerequisites:
    A project named "TestProject1" already exists

Step:
    Send a request to update the description of a work package.
    Use a unique string to set as the new
    The work package should be created under the "TestProject1" project.

Expected Result:
    1. Response status: 200
    2. Response contains a "work package" object with description matching the value set in the request
"""

from config.api import API
from framework.api.work_packages_api import WorkPackagesApi


def test_007_create_work_package():
    data = {
        "subject": API.TEST_007["WORK_PACKAGE_SUBJECT"],
        "description": {
            "raw": API.TEST_007["WORK_PACKAGE_DESC"]
        },
        "_links": {
            "project": {
                "href": f'/api/v3/projects/{API.TEST_001["PROJECT_ID"]}'
            }
        }
    }

    # Send POST request
    actual = WorkPackagesApi(API.BASE_URL, API.API_KEY).create_work_package(data)
    # Parse response to json format
    actual_data = actual.json()

    # Validate status code
    assert actual.status_code == 201, "Failed to get correct response code"
    # Validate work package subject
    assert actual_data["subject"] == API.TEST_007["WORK_PACKAGE_SUBJECT"], "Failed to get correct work package subject"
