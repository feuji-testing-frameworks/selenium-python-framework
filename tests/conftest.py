import configparser
import json
import os
import pytest
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, '..', 'config', 'config.ini')
api_data_path = os.path.join(current_dir, '..', 'data', 'api_data.json')


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
