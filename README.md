Project Name

Selenium-Python-Framework

Description

This project is a combination of UI, API, and mobile automation tests using Python-Selenium in the Pytest framework. It includes tests for various functionalities across different platforms.

Prerequisites

Before running the tests, make sure you have the following installed:
Python (version 3.12.1)
Android Studio( 2023.2.1)
Appium(2.5.2)
Appium Inspector(2024.2.2)
IDE (PyCharm, VSCode, etc.)
Additionally, ensure you have the following setup:

1. Clone the Project:
    Clone the project repository from GitHub using the following command:
    https://github.com/feuji-testing-frameworks/selenium-python-framework.git
2. Create a Virtual Environment:
    Navigate to the project directory and create a virtual environment using the following command:
    python -m venv venv
3. Activate the Virtual Environment:
    venv\Scripts\activate
4. Install Dependencies: Install the required dependencies by running the following command:
    pip install -r requirements.txt
5. Run the Tests: Execute the tests using the following command:
    pytest -s --alluredir=allure-report
6. Run the tests concurrently: Execute the tests using the following command:
    python ./tests/run_tests_concurrently.py 
6. View Test Reports: After running the tests, you can view the test reports using Allure. Run the following command to
serve the reports:
    allure serve allure-report
