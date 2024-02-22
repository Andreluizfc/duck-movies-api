import os
from api.db_manager import db_manager
from api import QUERIES_PATH


def get_min_max_wins_intervals():
    """Retrieve information about minimum and maximum prize intervals for winning producers.

    Executes a SQL query to fetch data from the 'movies' table, identifying winning producers' prize intervals.
    The result is processed to find both the minimum and maximum prize intervals, and the information is organized
    into a dictionary containing two lists: 'min' and 'max'.

    Returns:
        dict: A dictionary containing information about minimum and maximum prize intervals for producers.
              The structure of the dictionary follows the specified format.

    Example:
        ```
        {
            "min": [
                {
                    "producers": "Producer 1",
                    "interval": 1,
                    "prev_win_year": 2008,
                    "win_year": 2009
                },
                {
                    "producers": "Producer 2",
                    "interval": 1,
                    "prev_win_year": 2018,
                    "win_year": 2019
                }
            ],
            "max": [
                {
                    "producers": "Producer 1",
                    "interval": 99,
                    "prev_win_year": 1900,
                    "win_year": 1999
                },
                {
                    "producers": "Producer 2",
                    "interval": 99,
                    "prev_win_year": 2000,
                    "win_year": 2099
                }
            ]
        }
        ```
    """

    # Read the SQL query from the file
    with open(os.path.join(QUERIES_PATH, "select_win_intervals.sql"), "r") as file:
        query = file.read()

    result_df = db_manager.conn.execute(query).fetchdf()

    result_dict = {"min": [], "max": []}

    if not result_df.empty:
        min_df = result_df[result_df["interval"] == result_df["interval"].min()]
        max_df = result_df[result_df["interval"] == result_df["interval"].max()]

        result_dict["min"] = min_df[
            ["producers", "interval", "prev_win_year", "win_year"]
        ].to_dict(orient="records")
        result_dict["max"] = max_df[
            ["producers", "interval", "prev_win_year", "win_year"]
        ].to_dict(orient="records")

    return result_dict
