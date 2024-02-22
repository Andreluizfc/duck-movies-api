import duckdb
import pandas as pd
from api import CSV_FILE_PATH


class DatabaseManager:
    def __init__(self):
        """Manages an in-memory DuckDB database and initializes it with data from a CSV file.

        Attributes:
            conn (duckdb.DuckDBPyConnection): DuckDB connection object for the in-memory database.

        Usage:
            Create an instance of DatabaseManager to be used across the application.
            ```
            db_manager = DatabaseManager()
            ```
        """
        self.conn = duckdb.connect(database=":memory:")

    def initialize_database(self):
        """Reads data from a CSV file, processes it, and creates a 'movies' table in the database.

        Reads data from a CSV file specified by CSV_FILE_PATH, processes it by converting 'winner' column values
        from 'yes' and 'no' to True and False, respectively. The processed data is then used to create a 'movies'
        table in the in-memory DuckDB database.

        Returns:
            None

        Usage:
            ```
            db_manager = DatabaseManager()
            db_manager.initialize_database()
            ```
        """

        df = pd.read_csv(CSV_FILE_PATH, delimiter=";")
        df["winner"].fillna("no", inplace=True)
        df["winner"] = df["winner"].replace({"no": False, "yes": True})

        # Define the schema for the table
        schema = {
            "year": "INT",
            "title": "STRING",
            "studios": "STRING",
            "producers": "STRING",
            "winner": "BOOL",
        }

        # Use the to_sql method to create the table from the DataFrame with the specified schema
        df.to_sql("movies", self.conn, index=False, if_exists="replace", dtype=schema)


# Create an instance of DatabaseManager to be used across the application
db_manager = DatabaseManager()
