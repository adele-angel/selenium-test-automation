"""
Test 008 - API - Delete Work Package

Step:
    1. Send a request to create a new work package with a unique name
        Expected Result:
            1. Response status: 201
            2. Response contains a "work package" object with subject matching the value set in the request

    2. Delete the newly created work package. Send a request to delete a work package by ID
        Expected Result:
            1. Response status: 204

    3. Verify the work package was deleted by sending a request to get a work package by ID
        Expected Result:
            1. Response status: 404
            2. Response contains an error "message": "The requested resource could not be found."
"""

import json
import time
import requests
from requests.auth import HTTPBasicAuth
from config.api import TestAPI

headers = {'Content-Type': 'application/json'}
auth = HTTPBasicAuth('apikey', TestAPI.API_KEY)


def test_008_delete_project():
    pass


def create_work_package(work_package_name):
    payload = {
        "subject": work_package_name,
        "_links": {
            "project": {
                "href": "/api/v3/projects/3"
            }
        }
    }
    res = requests.post(TestAPI.BASE_URL + "/work_packages/", headers=headers, auth=auth, data=json.dumps(payload))
    return res


def delete_work_package(work_package_name):
    res = create_work_package(work_package_name)
    json_res = res.json()
    id = str(json_res["id"])
    response = requests.delete(TestAPI.BASE_URL + "/work_packages/" + id, headers=headers, auth=auth)
    return id


def test_create_work_package():
    work_package_name = "This is a new work package"
    res = create_work_package(work_package_name)
    assert res.status_code == 201, "Failed to get correct response code"
    json_res = res.json()
    assert json_res["subject"] == work_package_name, "Failed to get correct project name"


def test_delete_work_package():
    res = create_work_package("This is another work package")
    json_res = res.json()
    id = str(json_res["id"])
    res = requests.delete(TestAPI.BASE_URL + "/work_packages/" + id, headers=headers, auth=auth)
    assert res.status_code == 204, "Failed to get correct response code"


def test_delete_work_package_again():
    id = delete_work_package("This is yet another work package")
    time.sleep(5)
    res = requests.delete(TestAPI.BASE_URL + "/work_packages/" + id, headers=headers, auth=auth)
    # Validating response code
    assert res.status_code == 404, "Failed to get correct response code"
