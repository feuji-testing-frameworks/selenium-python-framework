import pytest
from appium.webdriver.appium_service import AppiumService
from appium.options.common import AppiumOptions
from selenium import webdriver
from typing import Dict,Any
import os
import configparser
import json
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, '..', 'config', 'config.ini')
api_data_path = os.path.join(current_dir, '..', 'data', 'api_data.json')
mobile_data_path = os.path.join(current_dir,'..','data','mobile_data.json')


@pytest.fixture
def api_data():
    with open(api_data_path, "r") as file:
        data = json.load(file)
    return data

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

def json_data(filepath) :
    with open(filepath, "r") as file :
        data = json.load(file)
    return data;

"""This function will provides the mobile data"""
@pytest.fixture
def mobile_data() :
    return json_data(mobile_data_path)

@pytest.fixture(scope="class", autouse=True)
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
    with open('data/ui_data.json',"r") as file :
        data = json.load(file)
    return data
