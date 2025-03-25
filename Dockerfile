# Use Python base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt (if you have one)
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application files into the container
COPY . .

# Command to run the unit tests
CMD ["python", "test_app.py"]

