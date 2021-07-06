"""
Test 006 - API - Update Work Package

Prerequisites:
    A "Task" work package with subject "My Task 1" already exists under a project named "TestProject1"

Step:
    Send a request to update the description of a work package.
    Use a unique string to set as the new

Expected Result:
    1. Response status: 200
    2. Response contains a "work package" object with description matching the value set in the request
"""

import pytest
import allure
from config.api import API
from framework.api.work_packages_api import WorkPackagesApi


@allure.title('Test 006 - API - Update Work Package')
@pytest.mark.t006
def test_006_update_work_package():
    data = {
        "description": {
            "raw": API.TEST_006["WORK_PACKAGE_DESC_UPD"]
        }
    }

    # Get work package by ID
    # Send GET request
    actual = WorkPackagesApi(API.BASE_URL, API.API_KEY).get_work_package(API.TEST_005["WORK_PACKAGE_ID"])
    actual_data = actual.json()
    data["lockVersion"] = actual_data["lockVersion"]
    # Validate status code
    assert actual.status_code == 200, f'Failed to send status code: {actual.status_code}'

    # Send PATCH request
    actual = WorkPackagesApi(API.BASE_URL, API.API_KEY).update_work_package(API.TEST_005["WORK_PACKAGE_ID"], data)
    # Parse response to json format
    actual_data = actual.json()

    # Validate status code
    assert actual.status_code == 200, f'Failed to send status code: {actual.status_code}'
    # Validate work package description
    assert actual_data["description"]["raw"] == API.TEST_006["WORK_PACKAGE_DESC_UPD"], f'Failed to get matching work package description: {actual_data["description"]["raw"]}'
