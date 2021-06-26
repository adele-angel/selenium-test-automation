import json
import pytest
import requests
from requests.auth import HTTPBasicAuth
from config.api import TestAPI


@pytest.fixture
def test_create_project():
    payload = {"name": "Hello World! @ 1234345435"}
    headers = {'Content-Type': 'application/json'}
    auth = HTTPBasicAuth('apikey', TestAPI.API_KEY)

    res = requests.post(TestAPI.BASE_URL + "/projects/", headers=headers, auth=auth, data=json.dumps(payload))

    # Validating response code
    assert res.status_code == 201, "Failed to get correct response code"
    # Parse response to json format
    json_res = res.json()
    # Validating project name
    assert json_res["name"] == "Hello World! @ 1234345435", "Failed to get correct project name"
    # Validating project description
    assert json_res["identifier"] == "hello-world-at-1234345435", "Failed to get correct project identifier"

    return str(json_res["id"])


@pytest.fixture
def test_delete_project(id):
    auth = HTTPBasicAuth('apikey', TestAPI.API_KEY)
    headers = {'Content-Type': 'application/json'}

    res = requests.delete(TestAPI.BASE_URL + "/projects/" + id, headers=headers, auth=auth)

    # Validating response code
    assert res.status_code == 204, "Failed to get correct response code"
    return id

@pytest.fixture
def test_delete_project_again(id):
    auth = HTTPBasicAuth('apikey', TestAPI.API_KEY)
    headers = {'Content-Type': 'application/json'}
    yield id
    res = requests.delete(TestAPI.BASE_URL + "/projects/" + id, headers=headers, auth=auth)

    # Validating response code
    assert res.status_code == 404, "Failed to get correct response code"
