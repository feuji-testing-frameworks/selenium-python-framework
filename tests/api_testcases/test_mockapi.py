import requests
from tests.conftest import *
import logging

class TestMockAPI:

    def test_get_all_bookings(self, api_config_from_ini, auth_token, mockapi_data, requests_mock):
        logging.info("Starting test_get_all_bookings")
        # Mocking the GET request to simulate the API response
        requests_mock.get(
            api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint'],
            json = mockapi_data.get('getbooking_data', []),
            status_code = 200,
            headers = {'Content-Type': 'application/json'},
            reason = 'OK'
        )
        logging.info("Mocking GET request to API")
        response = requests.get(api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint'], 
                                headers={'Cookie': 'token=' + auth_token})
        logging.info("Received response: %s", response.json())
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        data = response.json()
        assert any("bookingid" in booking for booking in data), "No bookings found"
        logging.info("Completed test_get_all_bookings")

    def test_create_booking(self, api_config_from_ini, auth_token, mockapi_data, requests_mock):
        logging.info("Starting test_create_booking")
        # Mocking the POST request to simulate the API response
        requests_mock.post(
            api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint'],
            json = mockapi_data.get('booking_data', {}),
            status_code = 200,
            reason = 'Created'
        )
        logging.info("Mocking POST request to API")
        response = requests.post(api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint'],
            json = mockapi_data.get('booking_data', {}), 
            headers = {'Cookie': 'token=' + auth_token}
        )
        logging.info("Received response: %s", response.json())
        assert response.status_code == 200
        assert response.reason == 'Created'
        logging.info("Completed test_create_booking")

    def test_update_booking(self, api_config_from_ini, auth_token, mockapi_data, create_booking_id, requests_mock):
        logging.info("Starting test_update_booking")
        # Mocking the PUT request to simulate the API response
        requests_mock.put(
            api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint'] + '/' + create_booking_id,
            json = mockapi_data.get('updated_booking_data',{}),
            status_code = 200
        )
        logging.info("Mocking PUT request to API")
        response = requests.put(api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint'] 
            + '/' + create_booking_id, json=mockapi_data.get('updated_booking_data', {}), 
            headers={'Cookie': 'token=' + auth_token}
        )
        logging.info("Received response: %s", response.json())
        assert response.status_code == 200
        data = response.json()
        assert data.get('firstname', "") == mockapi_data.get('updated_booking_data', {}).get('firstname', "")
        logging.info("Completed test_update_booking")

    def test_partial_update_booking(self, api_config_from_ini, auth_token, mockapi_data, create_booking_id, requests_mock):
        logging.info("Starting test_partial_update_booking")
        # Mocking the PATCH request to simulate the API response
        requests_mock.patch(
            api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint'] + '/' + create_booking_id,
            json = mockapi_data.get('patch_data',{}),
            status_code = 200
        )
        logging.info("Mocking PATCH request to API")
        response = requests.patch(api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint'] 
            + '/' + create_booking_id, json = mockapi_data.get('patch_data', {}),
            headers={'Cookie': 'token=' + auth_token}
        )
        logging.info("Received response: %s", response.json())
        assert response.status_code == 200
        data = response.json()
        assert data.get('lastname', "") == "Johnson"
        logging.info("Completed test_partial_update_booking")

    def test_delete_booking(self, api_config_from_ini, auth_token, create_booking_id, requests_mock):
        logging.info("Starting test_delete_booking")
        # Mocking the DELETE request to simulate the API response
        requests_mock.delete(
            api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint'] + '/' + create_booking_id,
            text='Booking deleted successfully',
            status_code=201
        )
        logging.info("Mocking DELETE request to API")
        response = requests.delete(api_config_from_ini['api_url'] + api_config_from_ini['booking_endpoint'] 
            + '/' + create_booking_id, headers={'Cookie': 'token=' + auth_token}
        )
        logging.info("Received response: %s", response.text)
        assert response.status_code == 201
        assert response.text == 'Booking deleted successfully'
        logging.info("Completed test_delete_booking")


