import logging
import pytest
import requests
from tests.conftest import *

@pytest.mark.usefixtures("api_config_from_ini", "auth_token", "api_data", "logger_setup")
class TestAPI:
   
    def test_get_all_bookings(self, api_config_from_ini, auth_token):
        response = requests.get(api_config_from_ini['api_url']+api_config_from_ini['booking_endpoint'], headers={'Cookie': 'token='+auth_token})
        assert response.status_code == 200
        data = response.json()
        assert any("bookingid" in booking for booking in data), "No bookings found"

 
    def test_create_booking(self, api_config_from_ini, auth_token, api_data):
        logging.info("Starting test_create_booking")
        assert auth_token is not None, "Auth token not found"
        response = requests.post(api_config_from_ini['api_url']+api_config_from_ini['booking_endpoint'], json=api_data.get('booking_data', {} ), headers={'Cookie': 'token='+auth_token})
        assert response.status_code == 200
        logging.info("Booking created successfully")
        data = response.json()
        assert data.get('bookingid', "") != ""
        logging.info("Ending test_create_booking")

    def test_update_booking(self, api_config_from_ini, auth_token, api_data, create_booking_id):
        assert create_booking_id is not None, "Booking ID not found"
        assert auth_token is not None, "Auth token not found"
        assert api_data is not None, "API data not found"
        logging.info(f"Updating booking with ID: {create_booking_id}")
        response = requests.put(api_config_from_ini['api_url']+api_config_from_ini['booking_endpoint']+ '/'+ create_booking_id , json=api_data.get('updated_booking_data', {} ), headers={'Cookie': 'token='+auth_token})
        assert response.status_code == 200, f"Failed to update booking. Status code: {response.status_code}"
        data = response.json()
        assert data.get('firstname', "") == api_data.get('updated_booking_data', {}).get('firstname', ""), f"First name not updated. Expected: {api_data.get('updated_booking_data', {}).get('firstname', '')}, Actual: {data.get('firstname', '')}"
        assert data.get('lastname', "") == api_data.get('updated_booking_data', {}).get('lastname', ""), f"Last name not updated. Expected: {api_data.get('updated_booking_data', {}).get('lastname', '')}, Actual: {data.get('lastname', '')}"
        logging.info("Booking updated successfully")

  
    def test_partial_update_booking(self, api_config_from_ini, auth_token, api_data, create_booking_id):
        assert create_booking_id is not None, "Booking ID not found"
        assert auth_token is not None, "Auth token not found"
        assert api_data is not None, "API data not found"
        logging.info(f"Partially updating booking with ID: {create_booking_id}")
        response = requests.patch(api_config_from_ini['api_url']+api_config_from_ini['booking_endpoint']+ '/'+ create_booking_id , json=api_data.get('patch_data', {} ), headers={'Cookie': 'token='+auth_token})
        assert response.status_code == 200, f"Failed to partially update booking. Status code: {response.status_code}"
        data = response.json()
        assert data.get('firstname', "") == api_data.get('patch_data', {}).get('firstname', ""), f"First name not updated. Expected: {api_data.get('patch_data', {}).get('firstname', '')}, Actual: {data.get('firstname', '')}"
        assert data.get('lastname', "") == api_data.get('patch_data', {}).get('lastname', ""), f"Last name not updated. Expected: {api_data.get('patch_data', {}).get('lastname', '')}, Actual: {data.get('lastname', '')}"
        logging.info("Booking partially updated successfully")


    def test_delete_booking(self, api_config_from_ini, auth_token, create_booking_id):
        assert create_booking_id is not None, "Booking ID not found"
        assert auth_token is not None, "Auth token not found"
        logging.info(f"Deleting booking with ID: {create_booking_id}")
        response = requests.delete(api_config_from_ini['api_url']+api_config_from_ini['booking_endpoint']+ '/'+ create_booking_id , headers={'Cookie': 'token='+auth_token})
        assert response.status_code == 201, f"Failed to delete booking. Status code: {response.status_code}"
        logging.info("Booking deleted successfully")
        logging.info("Ending test_delete_booking")
