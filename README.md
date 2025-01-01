# Tivit Test Project

This project is a FastAPI application that provides authentication and user management functionalities. It includes endpoints for user login, retrieving user information, and retrieving admin reports.

## Features

- User authentication with JWT tokens
- Role-based access control (user and admin)
- Endpoints to fetch user purchases and admin reports

## Setup

### Prerequisites

- [UV](https://docs.astral.sh/uv/) package and project manager

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/bimbaz/tivit_test.git
    cd tivit_test
    ```

2. Install dependencies and create a virtual environment using UV:

    ```sh
    uv sync
    ```

3. Create a `.env` file in the root directory and add the following environment variables. There is a `.env.example` file that you can use as a template.:

    ```env
    ACCESS_TOKEN_EXPIRE_MINUTES="30"
    SECRET_KEY="your_secret_key"
    ALGORITHM="HS256"
    ```

### Running the Application

1. Run the application using UV:

    ```sh
    uv run -m app.main
    ```

2. The application will be available at `http://localhost:8000`.

### Documentation

The API documentation is available at `http://localhost:8000/docs` or `http://localhost:8000/redoc`.


## API Endpoints

### Authentication

- `POST /token`: Authenticate a user and return a JWT token.

### User

- `GET /user`: Retrieve the current user's information and purchases. Requires a valid JWT token with the "user" role.

### Admin

- `GET /admin`: Retrieve the current admin's information and reports. Requires a valid JWT token with the "admin" role.

## License

This project is licensed under the MIT License.
