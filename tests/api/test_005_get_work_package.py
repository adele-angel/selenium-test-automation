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

import requests
from requests.auth import HTTPBasicAuth
from config.api import TestAPI


def test_005_get_work_package():
    # Send GET request
    res = requests.get(TestAPI.BASE_URL + "/work_packages/" + "34", auth=HTTPBasicAuth('apikey', TestAPI.API_KEY))

    # Validating response code
    assert res.status_code == 200, "Failed to get correct response code"

    # Parse response to json format
    json_res = res.json()

    # Validating work package type
    assert json_res["_embedded"]["type"]["name"] == "Task", "Failed to get correct work package type"

    # Validating work package subject
    assert json_res["subject"] == "My Task 1", "Failed to get correct work package subject"

    # Validating work package subject description
    assert json_res["description"][
               "raw"] == "This is the first task of TestProject1", "Failed to get correct work package description"
