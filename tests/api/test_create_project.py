import json

import requests
from requests.auth import HTTPBasicAuth
from config.api import TestAPI


def test_create_project():
    payload = {
        "name": "Hello World! @ 127"
    }

    headers = {'Content-Type': 'application/json'}
    auth = HTTPBasicAuth('apikey', TestAPI.API_KEY)

    res = requests.post(TestAPI.BASE_URL + "/projects/", headers=headers, auth=auth, data=json.dumps(payload))

    # Validating response code
    assert res.status_code == 201, "Failed to get correct response code"

    # Parse response to json format
    json_res = res.json()

    # Validating project name
    assert json_res["name"] == "Hello World! @ 127", "Failed to get correct project name"

    # Validating project description
    assert json_res["identifier"] == "hello-world-at-127", "Failed to get correct project identifier"
