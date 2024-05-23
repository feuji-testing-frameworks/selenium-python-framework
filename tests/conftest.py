import logging
import pytest
from appium.webdriver.appium_service import AppiumService
from appium.options.common import AppiumOptions
from selenium import webdriver
from typing import Dict,Any
import os
import configparser
import json
import requests
import logging
import allure
import shutil
from allure_commons.types import AttachmentType

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, '..', 'config', 'config.ini')
api_data_path = os.path.join(current_dir, '..', 'data', 'api_data.json')
mobile_data_path = os.path.join(current_dir,'..','data','mobile_data.json')
ui_data_path = os.path.join(current_dir,'..','data','ui_data.json')

#This fixtures are used for api
"""API fixtures are started"""
@pytest.fixture
def api_data():
    return json_data(api_data_path);

@pytest.fixture(scope='function')
def api_config_from_ini():
    configParser = configparser.ConfigParser()
    configParser.read(config_path, encoding='utf-8')
    if configParser.has_section('API'):
        config = dict(configParser.items('API'))
    else:
        raise ValueError("API section not found in the config file")
    return config


@pytest.fixture(scope='function')
def auth_token(api_data, api_config_from_ini):
    response = requests.post(api_config_from_ini['api_url']+api_config_from_ini['auth_endpoint'],
                             json=api_data.get('auth_payload', {} ))
    return response.json().get('token', "")

@pytest.fixture(scope='function')
def create_booking_id(api_data, api_config_from_ini, auth_token):
    response = requests.post(api_config_from_ini['api_url']+api_config_from_ini['booking_endpoint'],
                             json=api_data.get('booking_data',{}), headers={'Cookie': 'token='+auth_token})
    assert response.status_code == 200, f"Failed to create booking: {response.text}"
    return str(response.json().get('bookingid', ""))
"""API fixtures are ended"""

"""MObile fixtures are started"""
"""This function provides the data for the mobile automation"""
def read_mobile_configuration() :
    configuration = configparser.ConfigParser();
    configuration.read(config_path)
    if 'Mobile' in configuration :
        mobile_configuration = configuration['Mobile']
        return mobile_configuration
    else :
        raise Exception("Mobile section is not found in config.ini")
    
"""This function provides the driver for the mobile automation"""
@pytest.fixture(scope='session')
def appium_driver_setup(request) :
    mobile_configuration = read_mobile_configuration();
    appium_server = AppiumService();
    appium_server.start();
    capabilities : Dict[str , Any ] = {
        "platformName" : mobile_configuration["platformName"],
        "appium:deviceName" : mobile_configuration["deviceName"],
        "appium:automationName" : mobile_configuration["automationName"],
        "appium:appPackage" : mobile_configuration["appPackage"],
        "appium:appActivity" : mobile_configuration["appActivity"],
        "appium:platformVersion" : mobile_configuration["platformVersion"],
        "appium:appPath" : mobile_configuration["appPath"]
    }
    driver = webdriver.Remote(mobile_configuration["appium_server_url"], options= AppiumOptions().load_capabilities(capabilities));
    yield driver
    driver.quit();
    appium_server.stop();

"""This function will provides the mobile data"""
@pytest.fixture
def mobile_data() :
    return json_data(mobile_data_path)
"""Mobile fixtures are ended"""

#This function is used to return the data from the json file common for ui,api,mobile
def json_data(filepath) :
    with open(filepath, "r") as file :
        data = json.load(file)
    return data;




"""UI fixtures are Started"""
@pytest.fixture(scope="class")
def browser_setup(request):
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    # Pass the Service instance to webdriver.Chrome()
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    request.cls.driver.maximize_window()
    config = read_config();
    ui_base_url = config["ui_base_url"]
    driver.get(ui_base_url);
    yield driver;
    driver.quit();

def read_config(ui_path=config_path, section='UI'):
    parser = configparser.ConfigParser();
    parser.read(ui_path, encoding='utf-8');
    if parser.has_section(section):
        config = dict(parser.items(section));
    else:
        raise ValueError(f"Section '{section}' not found in the config file.");
    return config;

@pytest.fixture
def ui_data():
    return json_data(ui_data_path)

@pytest.fixture(scope='function', autouse=True)
def logger_setup(request):
    # Configuring root logger
    logger_name = "root"
    root_logger = logging.getLogger(logger_name)
    root_logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s : %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    # Adding console handler for displaying logs in the console
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    root_logger.addHandler(ch)
    # Creating log folder and file
    log_folder = os.path.abspath(os.path.join(current_dir, '..', 'Log'))  # Assuming 'Log' folder is located one level up
    try:
        os.makedirs(log_folder, exist_ok=True)
        log_file = os.path.join(log_folder, 'test_logs.log')
        fh = logging.FileHandler(log_file)
        fh.setFormatter(formatter)
        root_logger.addHandler(fh)
        print("Log folder and file created successfully.")
    except Exception as e:
        print(f"Error creating log folder or file: {e}")
    # Adjusting logging levels for specific loggers
    webdriver_logger = logging.getLogger('selenium.webdriver')  # Adjusting logging level for selenium.webdriver logger
    webdriver_logger.setLevel(logging.WARNING)
    urllib3_logger = logging.getLogger('urllib3')  # Adjusting logging level for urllib3 logger
    urllib3_logger.setLevel(logging.WARNING)
    yield  # Executing test functions
    # Cleaning up log handlers to avoid duplicate log entries
    root_logger.removeHandler(ch)
    if fh:
        root_logger.removeHandler(fh)
        fh.close()

#  Allure Report
# @pytest.fixture()
# def log_on_failure(request):
#     yield
#     item = request.node
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(),name="failed_test",attachment_type=AttachmentType.PNG)
@pytest.fixture(autouse= True)
def log_on_failure(request):
    yield
    item = request.node
    if hasattr(item, "rep_call") and hasattr(item.rep_call, "failed") and item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=allure.attachment_type.PNG)

def clean_allure_reports(report_dir):
    """
    Clean previous generated Allure reports.

    Args:
        report_dir (str): Path to the directory containing the Allure reports.
    """
    if os.path.exists(report_dir):
        try:
            shutil.rmtree(report_dir)
            print("Previous Allure reports deleted successfully.")
        except Exception as e:
            print(f"Error while deleting previous Allure reports: {e}")
    else:
        print("No previous Allure reports found.")

# Example usage:
report_directory = "allure_reports"
clean_allure_reports(report_directory)
"""UI fixtures are ended"""