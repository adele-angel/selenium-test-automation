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

import json
import requests
from requests.auth import HTTPBasicAuth
from config.api import TestAPI


def test_create_work_package():
    payload = {
        "subject": "THIS IS A NEW TASK!"
    }

    headers = {'Content-Type': 'application/json'}
    auth = HTTPBasicAuth('apikey', TestAPI.API_KEY)

    res = requests.post(TestAPI.BASE_URL + "/projects/3/work_packages", headers=headers, auth=auth,
                        data=json.dumps(payload))

    # Validating response code
    assert res.status_code == 201, "Failed to get correct response code"

    # Parse response to json format
    json_res = res.json()

    # Validating work package subject
    assert json_res["subject"] == payload["subject"], "Failed to get correct work package subject"
