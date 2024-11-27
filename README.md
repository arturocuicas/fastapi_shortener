# fastapi_shortener

## Description

`fastapi_shortener` is a web application built with FastAPI that allows shortening URLs and redirecting users to the original URLs using a unique hash.

## Features

- **FastAPI**: Uses the FastAPI framework to build the API.
- **Redis**: Uses Redis for caching shortened URLs.
- **MongoDB**: Uses MongoDB for persistent storage of URLs.
- **Pickle**: Serializes and deserializes URL data using Pickle.

## Installation

1. Clone the repository:
    ```bash
    git clone <REPOSITORY_URL>
    cd fastapi_shortener
    ```

2. 

2. Access the interactive API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Endpoints

- **GET /**: Root endpoint that returns a greeting message.
- **GET /{hash_key}**: Redirects to the original URL associated with the `hash_key`.

## Configuration

The application configuration is located in the `core/config.py` file. You can adjust parameters such as the application title, version, and documentation URLs.

## Dependencies

- **FastAPI**: Framework for building fast and efficient APIs.
- **Redis**: In-memory database used for caching.
- **MongoDB**: NoSQL database used for persistent storage.
- **Pickle**: Library for serializing and deserializing Python objects.

## Contributions

Contributions are welcome. Please open an issue or a pull request to discuss any changes you would like to make.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.