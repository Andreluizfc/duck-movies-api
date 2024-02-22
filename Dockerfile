# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the PYTHONPATH to include the /app folder
ENV PYTHONPATH=/app:$PYTHONPATH

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run your application
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]