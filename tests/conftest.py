import pytest
from appium.webdriver.appium_service import AppiumService
from appium.options.common import AppiumOptions
from selenium import webdriver
from typing import Dict,Any
import os
import configparser
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir,'..','config', 'config.ini')
mobile_data_path = os.path.join(current_dir,'..','data','mobile_data.json')

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
    with open(mobile_data_path , "r") as file :
        data = json.load(file)
    return data;