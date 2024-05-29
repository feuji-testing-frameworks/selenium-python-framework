# Selenium python Framework

## Description

This project is a combination of UI, API, and mobile automation tests using Python-Selenium in the Pytest framework. It includes tests for various functionalities across different platforms.

## Prerequisites

Before running the tests, make sure you have the following installed:

- Python (version 3.12.1)
- Android Studio( 2023.2.1)
- Appium(2.5.2)
- Appium Inspector(2024.2.2)
- IDE (PyCharm, VSCode, etc.)

Additionally, ensure you have the following setup:

1. **Clone the Project**: Clone the project repository from GitHub using the following command:

   `git clone https://github.com/feuji-testing-frameworks/selenium-python-framework.git`

2. **Create a Virtual Environment**: Navigate to the project directory and create a virtual environment:

   ` python -m venv venv`

3. **Activate the Virtual Environment**:

   `venv\Scripts\activate`

4. **Install Dependencies**: Install the required dependencies by running:

   `pip install -r requirements.txt`

## Running the Tests

- **Run the Tests**: Execute the tests using:
`pytest -s --alluredir=allure_report`

- **Run the Tests Concurrently**: Execute the tests concurrently using:
`python ./tests/run_tests_concurrently.py`

- **Run the Mobile Testcases Concurrently**: Execute the mobile testcases concurrently using :
`pytest -v -n 2   ./tests/mobile_testcases/test_mobile.py --alluredir="./allure_report"`

## Viewing Test Reports

After running the tests, view the test reports using Allure:

`allure serve allure_report`

This command will serve the reports for easy viewing and analysis.









   
