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

import json
import requests
from requests.auth import HTTPBasicAuth
from config.api import TestAPI


def test_update_project_by_id():

    payload = {
        "description": {
            "raw": "Let's update this project!"
        }
    }

    headers = {'Content-Type': 'application/json'}
    auth = HTTPBasicAuth('apikey', TestAPI.API_KEY)

    # TODO: check if the project exists

    # Send PATCH request
    res = requests.patch(TestAPI.BASE_URL + "/projects/" + TestAPI.PROJECT_ID, headers=headers,
                         auth=auth, data=json.dumps(payload))

    # Validating response code
    assert res.status_code == 200, "Failed to get correct response code"

    # Parse response to json format
    json_res = res.json()

    # Validating project name
    assert json_res["name"] == TestAPI.PROJECT_TITLE, "Failed to get correct project name"

    # Validating project description
    assert json_res["description"]["raw"] == TestAPI.PROJECT_DESC_UPD, "Failed to get correct project description"
