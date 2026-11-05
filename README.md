# Flask REST API Project

## Project Description

This project is a simple RESTful API developed using Python and Flask for my software development course.

The application provides two endpoints that allow users to retrieve information and submit new data using HTTP requests.

The purpose of this project is to practice backend development, API design, JSON responses, software testing, and Agile development techniques.

## Technologies Used

- Python
- Flask
- Requests library
- Git and GitHub
- GitHub Projects

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /hello | Returns a welcome message in JSON format |
| GET | /data | Returns a list of sample data |
| POST | /data | Accepts JSON data and adds a new item |

## How to Run the Application

1. Download or clone the GitHub repository.
2. Open the project folder in VS Code.
3. Create and activate a Python virtual environment.
4. Install the required libraries using `pip install -r requirements.txt`.
5. Start the Flask application using `python app.py`.
6. Open `http://127.0.0.1:5001/hello` in a browser.

## API Testing

The API was tested using Python's requests library.

The `test_api.py` script sends GET and POST requests and checks the HTTP response codes.

Testing results:

- GET /hello — 200 OK
- GET /data — 200 OK
- POST /data — 201 Created
- GET /data after POST — 200 OK

All automated tests passed successfully.

## Agile Development Process

Agile development techniques were used to organize and document the project.

A GitHub Projects Kanban board was created with three columns:

- Todo
- In Progress
- Done

User stories were created to represent the required application features.

### Development Iterations

**Iteration 1: Initial API Development**

- Set up the Python virtual environment.
- Installed Flask.
- Created the /hello endpoint.
- Created the GET /data endpoint.

**Iteration 2: API Testing and Improvements**

- Implemented POST functionality.
- Created an automated testing script.
- Tested GET and POST requests.
- Resolved an issue with port 5000 by switching to port 5001.

**Iteration 3: Documentation and Version Control**

- Uploaded the project to GitHub.
- Corrected an issue where the virtual environment was accidentally tracked by Git.
- Created a GitHub Projects Kanban board.
- Added user stories and documented development progress.

### Agile Retrospective

During development, testing revealed issues that required troubleshooting.

One issue involved receiving an HTTP 403 response when attempting to access the API on port 5000. Changing the application to port 5001 resolved the problem.

Another issue occurred when the Python virtual environment was accidentally uploaded to GitHub. This was corrected by updating the .gitignore file and removing the folder from Git tracking.

These experiences demonstrated the importance of incremental testing, version control, and continuous improvement.

## Advantages and Challenges of Open-Source Software

Flask is an open-source web framework for Python.

**Advantages:**

- Free to use.
- Lightweight and relatively easy to learn.
- Supported by community documentation and resources.
- Flexible for developing APIs and web applications.

**Challenges:**

- Developers are responsible for selecting and configuring additional tools.
- Some advanced functionality requires third-party packages.
- Dependencies must be maintained and updated.
- Security and deployment configurations require additional attention.

Using Flask demonstrated how open-source software can support application development without expensive proprietary tools.

## Future Improvements

Possible future improvements include:

- Adding a database for permanent data storage.
- Implementing user authentication.
- Adding more API endpoints.
- Integrating the API into a larger AI-powered application.
