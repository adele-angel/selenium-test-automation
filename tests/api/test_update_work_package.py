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

import json
import requests
from requests.auth import HTTPBasicAuth
from config.api import TestAPI


def test_update_work_package():
    payload = {
        "lockVersion": 2,
        "description": {
            "raw": "This is updated description for task 1!"
        }
    }

    headers = {'Content-Type': 'application/json'}
    auth = HTTPBasicAuth('apikey', TestAPI.API_KEY)

    # Send PATCH request
    res = requests.patch(TestAPI.BASE_URL + "/work_packages/" + "34", headers=headers,
                         auth=auth, data=json.dumps(payload))

    # Validating response code
    assert res.status_code == 200, "Failed to get correct response code"

    # Parse response to json format
    json_res = res.json()

    # Validating response object
    assert json_res, "Failed to get work package object"

    # Validating work package description
    assert json_res["description"]["raw"] == payload["description"][
        "raw"], "Failed to get correct work package description"
