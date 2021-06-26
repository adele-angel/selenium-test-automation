import json

import requests
from requests.auth import HTTPBasicAuth
from config.api import TestAPI


def test_update_project_by_id():
    # Send GET request
    payload = {
        "description": {
            "raw": "Let's update this project!"
        }
    }

    headers = {'Content-Type': 'application/json'}
    auth = HTTPBasicAuth('apikey', TestAPI.API_KEY)

    # TODO: check if the project exists

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
