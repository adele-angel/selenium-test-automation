rem Run all tests and create allure reports

call venv\scripts\activate

pytest -v -s --alluredir=/reports tests
pytest --alluredir=/reports/allure_results
allure serve /reports/allure_results
