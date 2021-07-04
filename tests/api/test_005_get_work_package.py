"""
Test 005 - API - Get Work Package by ID

Prerequisites:
    A "Task" work package with subject "My Task 1" already exists under a project named "TestProject1"

Step:
    Send a request to get a work package by ID. Use the ID of "My Task 1"

Expected Result:
    1. Response status: 200
    2. Work package type is "Task"
    3. Work package subject is "My Task 1"
"""

from config.api import API
from framework.api.work_packages_api import WorkPackagesApi


def test_005_get_work_package():
    """
    This test function sends an http 'GET' request to the server
    and checks if response is valid
    :return: None
    """
    # Send GET request
    actual = WorkPackagesApi(API.BASE_URL, API.API_KEY).get_work_package(API.TEST_005["WORK_PACKAGE_ID"])
    # Parse response to json format
    actual_data = actual.json()

    # Validate status code
    assert actual.status_code == 200, f'Failed to send status code {actual.status_code}'
    # Validate work package type
    assert actual_data["_embedded"]["type"]["name"] == API.TEST_005["WORK_PACKAGE_TYPE"], "Failed to get correct work package type"
    # Validate work package subject
    assert actual_data["subject"] == API.TEST_005["WORK_PACKAGE_SUBJECT"], "Failed to get correct work package subject"
