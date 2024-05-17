
import requests
from tests.conftest import *
import logging
from requests.exceptions import RequestException
import pytest

class TestMockAPI:

    def test_get_all_bookings(self, api_config_from_ini, auth_token, requests_mock):
        # Mocking the GET request to simulate the API response
        requests_mock.get(
            api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint'],
            json=[{"bookingid": 1, "firstname": "John", "lastname": "Doe"},
                    {"bookingid": 2, "firstname": "Jane", "lastname": "Smith"},
                    {"bookingid": "123", "firstname": "John Doe"}],
            status_code=200,
            headers={'Content-Type': 'application/json'},
            reason='OK'
        )
        response = requests.get(api_config_from_ini['api_url']+api_config_from_ini['booking_endpoint'], headers={'Cookie': 'token='+auth_token})
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        data = response.json()
        assert any("bookingid" in booking for booking in data), "No bookings found"

    def test_create_booking(self, api_config_from_ini, auth_token, api_data, requests_mock):
        # Mocking the POST request to simulate the API response
        requests_mock.post(
            api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint'],
            json={"bookingid": 3, "firstname": "Alice", "lastname": "Smith"},
            status_code=200,
            reason='Created'
        )
        response = requests.post(api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint'], json=api_data.get('booking_data', {}), headers={'Cookie': 'token='+auth_token})
        assert response.status_code == 200
        data = response.json()
        assert data.get('bookingid', "") == 3
        assert response.reason == 'Created'

    def test_update_booking(self, api_config_from_ini, auth_token, api_data, create_booking_id, requests_mock):
        # Mocking the PUT request to simulate the API response
        requests_mock.put(
            api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint']+ '/'+ create_booking_id ,
            json={"firstname": "Bob", "lastname": "Jones"},
            status_code=200
        )
        response = requests.put(api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint']+ '/'+ create_booking_id , json=api_data.get('updated_booking_data', {}), headers={'Cookie': 'token='+auth_token})
        assert response.status_code == 200
        data = response.json()
        assert data.get('firstname', "") == "Bob"

    def test_partial_update_booking(self, api_config_from_ini, auth_token, api_data, create_booking_id, requests_mock):
        # Mocking the PATCH request to simulate the API response
        requests_mock.patch(
            api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint']+ '/'+ create_booking_id ,
            json={"lastname": "Johnson"},
            status_code=200
        )

        response = requests.patch(api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint']+ '/'+ create_booking_id , json=api_data.get('patch_data', {}), headers={'Cookie': 'token='+auth_token})
        assert response.status_code == 200
        data = response.json()
        assert data.get('lastname', "") == "Johnson"

    def test_delete_booking(self, api_config_from_ini, auth_token, create_booking_id, requests_mock):
        # Mocking the DELETE request to simulate the API response
        requests_mock.delete(
            api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint']+ '/'+ create_booking_id ,
            text = 'Booking deleted successfully',
            status_code=201
        )

        response = requests.delete(api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint']+ '/'+ create_booking_id , headers={'Cookie': 'token='+auth_token})
        assert response.status_code == 201
        assert response.text == 'Booking deleted successfully'

