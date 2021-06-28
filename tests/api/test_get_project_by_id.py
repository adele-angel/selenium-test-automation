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

import requests
from requests.auth import HTTPBasicAuth
from config.api import TestAPI


def test_get_project_by_id():
    # Send GET request
    res = requests.get(TestAPI.BASE_URL + "/projects/" + TestAPI.PROJECT_ID,
                       auth=HTTPBasicAuth('apikey', TestAPI.API_KEY))

    # Validating response code
    assert res.status_code == 200, "Failed to get correct response code"

    # Parse response to json format
    json_res = res.json()

    # Validating project name
    assert json_res["name"] == TestAPI.PROJECT_TITLE, "Failed to get correct project name"

    # Validating project description
    assert json_res["description"]["raw"] == TestAPI.PROJECT_DESC, "Failed to get correct project description"
