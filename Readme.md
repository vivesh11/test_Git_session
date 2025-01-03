# Flask API Project

This is a simple Flask API with Docker and test cases using `pytest`.

## Features
- Flask API with the following endpoints:
  - `/` - Home endpoint that returns a welcome message.
  - `/users` - Get all users.
  - `/user/<id>` - Get a specific user by ID.
  - `/user` - Create a new user.
  
- Test cases for all endpoints using `pytest`.

## Requirements
- Docker
- Docker Compose
- Python 3.9+

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/flask_api_project.git
   cd flask_api_project

2. Build and run the app and tests using Docker Compose:
   ```bash
   docker-compose up --build -d

3. Access the API:
   - Navigate to http://localhost:5050 to see the Flask API running.
   - To get all users, make a GET request to `http://localhost:5050/users`.

4. To run the tests, you can stop the app and run:
   ```bash
   docker-compose run pytest

5. Stopping the containers:
   ```bash
   docker-compose down

### Conclusion
You’ve successfully updated the project to use port `5050` for the Flask app. Now you can run the API and the test cases using Docker Compose. The app should be accessible on `http://localhost:5050`.
