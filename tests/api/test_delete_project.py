"""
Test 004 - API - Delete Project

Step:
    1. Send a request to create a new project with a unique name
        Expected Result:
            1. Response status: 201
            2. Response contains a "project" object with name and identifier matching the value set in the request

    2. Delete the newly created project. Send a request to delete a project by ID
        Expected Result:
            1. Response status: 204

    3. Verify the project was deleted by sending a request to get a project by ID
        Expected Result:
            1. Response status: 404
            2. Response contains an error "message": "Work packages in non descendant projects reference versions of the project or its descendants."
"""

import json
import time
import requests
from requests.auth import HTTPBasicAuth
from config.api import TestAPI


def create_project(project_name):
    payload = {"name": project_name}
    headers = {'Content-Type': 'application/json'}
    auth = HTTPBasicAuth('apikey', TestAPI.API_KEY)

    res = requests.post(TestAPI.BASE_URL + "/projects/", headers=headers, auth=auth, data=json.dumps(payload))
    return res


def delete_project(project_name):
    headers = {'Content-Type': 'application/json'}
    auth = HTTPBasicAuth('apikey', TestAPI.API_KEY)
    res = create_project(project_name)
    json_res = res.json()
    id = str(json_res["id"])
    response = requests.delete(TestAPI.BASE_URL + "/projects/" + id, headers=headers, auth=auth)
    assert response.status_code == 204
    return id


def test_create_project():
    res = create_project("sdd")

    # Validating response code
    assert res.status_code == 201, "Failed to get correct response code"
    # Parse response to json format
    json_res = res.json()
    # Validating project name
    assert json_res["name"] == "sdd", "Failed to get correct project name"
    # Validating project description
    assert json_res["identifier"] == "sdd", "Failed to get correct project identifier"


def test_delete_project():
    res = create_project("Hlloosfgdddrefggffsss2f")
    json_res = res.json()
    id = str(json_res["id"])

    auth = HTTPBasicAuth('apikey', TestAPI.API_KEY)
    headers = {'Content-Type': 'application/json'}

    res = requests.delete(TestAPI.BASE_URL + "/projects/" + id, headers=headers, auth=auth)

    # Validating response code
    assert res.status_code == 204, "Failed to get correct response code"


def test_delete_project_again():
    id = delete_project("pggpehfdfo")
    time.sleep(5)

    auth = HTTPBasicAuth('apikey', TestAPI.API_KEY)
    headers = {'Content-Type': 'application/json'}
    res = requests.delete(TestAPI.BASE_URL + "/projects/" + id, headers=headers, auth=auth)

    # Validating response code
    assert res.status_code == 404, "Failed to get correct response code"
