import os


# Get the path of the current directory (directory containing this __init__.py file)
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# Path for loading data
CSV_FILE_PATH = os.path.join(ROOT_PATH, "data", "movieslist.csv")

# Path for loading queries
QUERIES_PATH = os.path.join(ROOT_PATH, "queries")
