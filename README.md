# How to Run the App with Docker

## Prerequisites:

- **Docker:** Ensure that Docker is installed on your machine. You can download Docker from the official website: [Docker](https://www.docker.com/get-started)

## Step-by-Step Instructions:

1. **Clone the Repository:**

    Open a terminal and run the following commands:

    ```bash
    git clone https://github.com/Andreluizfc/duck-movies-api.git
    cd duck-movies-api
    ```

2. **Build the Docker Image:**

    Run the following command to build the Docker image:

    ```bash
    docker-compose build
    ```

3. **Run the FastAPI Application:**

    Start the FastAPI application with the following command:
    
        ```bash
        docker-compose up run_api
        ```
    Wait until you see logs indicating that the application is running.

4. **Run Tests:**
    
    Ensure that the FastAPI application is fully started before running the tests.

    Execute the tests with the following command:

    ```bash
    docker-compose up run_tests
    ```
   
## Access the API:

    Once the application is running, access the API at http://0.0.0.0:8000 in your browser or use tools like curl or Postman to interact with the API.

## Notes:
    If you encounter issues, make sure Docker is properly installed, and there are no port conflicts on your machine.

    If the route http://0.0.0.0:8000 in unnacessbile, try to run the app in http://127.0.0.1 changing it in the docker-compose.yaml file
    