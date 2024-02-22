# main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from api import db_utils
from api.db_manager import db_manager

app = FastAPI()


# Default route
@app.get("/")
async def read_root():
    """Default route to get a simple greeting.

    Returns:
        dict: A dictionary containing a greeting message.
    """
    return {"message": "Hello, World!"}


# Event handler to populate the database when the application starts
@app.on_event("startup")
async def startup_event():
    """Event handler to populate the database when the application starts.

    Initializes the in-memory DuckDB database using the DatabaseManager's `initialize_database` method.
    """
    db_manager.initialize_database()


# Endpoint to get both producer scenarios
@app.get("/prize_intervals", response_model=dict)
async def get_prize_intervals():
    """Endpoint to get both producer scenarios - minimum and maximum prize intervals.

    Returns:
        dict: A dictionary containing information about minimum and maximum prize intervals for producers.

    Raises:
        HTTPException: If an internal server error occurs during the process.
    """
    try:
        min_max_intervals = db_utils.get_min_max_wins_intervals()
        return JSONResponse(content=min_max_intervals)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


# To run for debug porposes
if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application using Uvicorn in debug mode
    uvicorn.run(app, host="127.0.0.1", port=8080, log_level="debug")
