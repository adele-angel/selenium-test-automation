rem Run all tests, create & view allure report

call venv\scripts\activate

pytest -v -s --alluredir=reports
allure serve reports
