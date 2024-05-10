import os
import pytest
from selenium import webdriver
import configparser
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir,'..','config', 'config.ini')

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