import pytest
import requests

# Test for unauthorized access (expected 401)
def test_users_unauthorized(mocker):
    # Define the URL and parameters inside the test function
    URL = "http://127.0.0.1:8000/users"
    params = {
        'username': 'admin',
        'password': 'admin'
    }

    # Create a mocked response and set its attributes
    mocked_response = mocker.Mock()
    mocked_response.status_code = 401
    mocked_response.text = ' '

    # Mock the requests.get method to return the mocked response
    mocker.patch('requests.get', return_value=mocked_response)

    # Send a GET request to the /users endpoint
    response = requests.get(URL, params=params)
    
    # Assert the status code is 401
    assert response.status_code == 401, f"Expected 401, but got {response.status_code}"
    
    # Assert the response body is empty (stripped of whitespace)
    assert response.text.strip() == "", f"Expected empty response body, but got: {response.text.strip()}"

# Test for authorized access with 'querty' (expected 200)
def test_users_authorized_with_querty(mocker):
    # Define the URL and parameters for a different test case
    URL = "http://127.0.0.1:8000/users"
    params = {
        'username': 'admin',
        'password': 'querty'
    }

    # Create a mocked response and set its attributes
    mocked_response = mocker.Mock()
    mocked_response.status_code = 200
    mocked_response.text = ' '

    # Mock the requests.get method to return the mocked response
    mocker.patch('requests.get', return_value=mocked_response)

    # Send a GET request to the /users endpoint
    response = requests.get(URL, params=params)
    
    # Assert the status code is 200
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    
    # Assert the response body is empty (stripped of whitespace)
    assert response.text.strip() == "", f"Expected empty response body, but got: {response.text.strip()}"