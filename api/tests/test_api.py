import requests
import pytest
from api.db_manager import db_manager

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

@pytest.fixture(autouse=True, scope="session")
def initialize_database():
    db_manager.initialize_database()


@pytest.fixture
def base_url():
    return "run_api:8000"


@pytest.fixture
def duckdb_cursor():
    # Assuming db_manager.conn is an active connection in your application
    connection = db_manager.conn
    cursor = connection.cursor()
    yield cursor
    cursor.close()


def test_hello_app(base_url):
    response = requests.get(f"http://{base_url}/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_get_prize_intervals(base_url):
    # Make a request to the API
    response = requests.get(f"http://{base_url}/prize_intervals")

    # Check if the request was successful (status code 200)
    assert response.status_code == 200

    # Parse the response JSON
    result = response.json()

    # Compare the result with the expected_result
    assert result == expected_result


def test_movies_table_exists(duckdb_cursor):
    cursor = duckdb_cursor
    duckdb_cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    assert ("movies",) in tables


def test_movies_table_schema(duckdb_cursor):
    cursor = duckdb_cursor
    cursor.execute("DESCRIBE movies")
    columns = cursor.fetchall()
    expected_schema = {
        "year": "INTEGER",
        "title": "VARCHAR",
        "studios": "VARCHAR",
        "producers": "VARCHAR",
        "winner": "BOOLEAN",
    }

    actual_schema = {col[0]: col[1] for col in columns}
    assert actual_schema == expected_schema


# Run the tests
if __name__ == "__main__":
    pytest.main(["-v", "test_api.py"])
