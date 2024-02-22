import requests
import pytest
import time

# Define the expected result
expected_result = {
    "min": [
        {
            "producers": "Andre Castro",
            "interval": 1,
            "prev_win_year": 2008,
            "win_year": 2009,
        },
        {
            "producers": "Cruiser Castro",
            "interval": 1,
            "prev_win_year": 2018,
            "win_year": 2019,
        },
        {
            "producers": "Jane Doe",
            "interval": 1,
            "prev_win_year": 2098,
            "win_year": 2099,
        },
    ],
    "max": [
        {
            "producers": "John Doe",
            "interval": 99,
            "prev_win_year": 1900,
            "win_year": 1999,
        }
    ],
}

# Define the FastAPI base URL
base_url = "run_api:8000"

# Introduce a small delay to wait apt start
time.sleep(10)


def test_get_prize_intervals():
    # Make a request to the API
    response = requests.get(f"http://{base_url}")
    response = requests.get(f"http://{base_url}/prize_intervals")

    # Check if the request was successful (status code 200)
    assert response.status_code == 200

    # Parse the response JSON
    result = response.json()

    # Compare the result with the expected_result
    assert result == expected_result


# Run the tests
if __name__ == "__main__":
    pytest.main(["-v", "test_api.py"])
