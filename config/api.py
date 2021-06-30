class API:
    # API Credentials
    PORT = "8080"
    BASE_URL = f"http://localhost:{PORT}"
    API_KEY = "1552e088259db32ed06920ff938baeef913572bfa8b17728697808d4e9d0d51a"

    # Test 001 - API - Get Project by ID
    TEST_001 = {
        "PROJECT_ID": "4",
        "PROJECT_NAME": "TestProject1",
        "PROJECT_DESC": "This is the first test project!"
    }

    # Test 002 - API - Update Project
    TEST_002 = {
        "PROJECT_DESC_UPD": "Let's update this project!\nHere's a unique string: (,/#@$%) 1+1=2."
    }

    # Test 003 - API - Create Project
    TEST_003 = {
        "PROJECT_NAME": "@My 2nd Test Project!",
        "PROJECT_DESC": "This is yet another test project",
        "PROJECT_IDENTIFIER": "my-2nd-test-project"
    }

    # Test 004 - API - Delete Project
    TEST_004 = {
        "PROJECT_NAME": "$%^& My 3rd Test @ Project!",
        "PROJECT_DESC": "This test project is meant to be deleted"
    }

    # Test 005 - API - Get Work Package by ID
    TEST_005 = {
        "WORK_PACKAGE_ID": "34",
        "WORK_PACKAGE_TYPE": "Task",
        "WORK_PACKAGE_SUBJECT": "My Task 1"
    }

    # Test 006 - API - Update Work Package
    TEST_006 = {
        "WORK_PACKAGE_DESC_UPD": "This is updated task description\nHere's a unique string: (,/#@$%) 1+1=2.",
        "lockVersion": "2"
    }

    # Test 007 - API - Create Work Package
    TEST_007 = {
        "WORK_PACKAGE_SUBJECT": "My New Work Package!",
        "WORK_PACKAGE_DESC": "This work package description\nHere's a unique string: (,/#@$%) 1+1=2."
    }

    # Test 008 - API - Delete Work Package
    TEST_008 = {
        "WORK_PACKAGE_SUBJECT": "$%^& My @ Work Package!",
        "WORK_PACKAGE_DESC": "This work package description\nHere's a unique string: (,/#@$%) 1+1=2."
    }
