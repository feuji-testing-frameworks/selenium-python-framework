from tenacity import retry, stop_after_attempt, wait_fixed
import requests

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_with_retry(url, headers=None):
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def post_with_retry(url, json=None, headers=None):
    response = requests.post(url, json=json, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def put_with_retry(url, json=None, headers=None):
    response = requests.put(url, json=json, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def patch_with_retry(url, json=None, headers=None):
    response = requests.patch(url, json=json, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def delete_with_retry(url, headers=None):
    response = requests.delete(url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response
