# Python-gRPC-Users-Operations

Python-gRPC-Users-Operations is a Python gRPC application designed with a clean architecture provided by [Uncle Bob](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html). It utilizes SQLAlchemy ORM for database interactions and is structured to ensure maintainability, scalability, and testability.

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Technologies](#architecture)
- [Setup](#setup)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Overview

The goal of Python-gRPC-Users-Operations is to provide a robust and scalable gRPC service for user operations. The application is built following the clean architecture principles, ensuring a clear separation of concerns between different layers.

## Architecture

The project is structured into four main layers:

1. **Data Layer**: Contains SQLAlchemy models and repositories, handles CRUD operations and database interactions.
2. **Domain Layer**: Encapsulates business logic, use cases, and interfaces. Manages entities, enums, custom exceptions, and service interfaces.
3. **Application Layer**: Implements gRPC servicers and services, contains gRPC views and middlewares to facilitate communication between clients and business logic.
4. **Configuration Layer**: Manages application configurations like database settings and logging configurations.

### Component Flow

1. **gRPC Servicer Initialization**: Starts the unit of work, database connection, and logger.
2. **gRPC View Handling**: Converts protobuf messages into dictionaries.
3. **Service Layer Processing**: Validates the request payload and maps it to use case request objects.
4. **Domain Layer Execution**: Invokes use cases to perform business validation and interacts with repositories for CRUD operations.


## Technologies

- **Python 3.8+**: The programming language used for development.
- **gRPC**: For creating the RPC services.
- **Protobuf 3**: Used for defining the gRPC service and message structures.
- **SQLAlchemy ORM**: For database interactions.
- **Pydantic**: For data validation and settings management using Python typing.
- **Docker**: For containerizing the application.
- **Makefile**: For automating operations.
- **Environment Variables**: For configuration management.

## Setup

### Prerequisites

- Python 3.8+
- pip
- virtualenv (optional but recommended)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/BadrTarek/grpc-users-ops
    cd grpc-users-ops
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    make install
    ```

4. **Generate Compiled Protobufs Files**:
    ```bash
    make generate-protos
    ```

5. **Configure the application**:
    Create a copy of the [.env.example](./src/grpc_user_ops/config/.env.example) file, rename it to **.env** in the same path, and add your environment variable values.

    Example `.env`:
    ```YAML
    DB_NAME=YOUR_DB_NAME
    DB_PASS=YOUR_DB_PASSWORD
    DB_PORT=5432
    DB_HOST=localhost
    ```

### Database Setup

1. **Create the database tables**:
    ```bash
    make migrate
    ```

## Usage

1. **Run the gRPC server**:
    ```bash
    make run
    ```

2. **Using the gRPC client**:
    You can create a gRPC client to interact with the server. An example client script might look like this:

    ```python
    import grpc
    import user_pb2
    import user_pb2_grpc

    def run():
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = user_pb2_grpc.UserServiceStub(channel)
            response = stub.CreateUser(user_pb2.UserRequest(username='testuser', email='test@example.com'))
            print("User created with ID:", response.id)

    if __name__ == '__main__':
        run()
    ```

## Testing

1. **Run the unit tests**:
    ```bash
    make unit-test
    ```
2. **Run the integration tests**:
    ```bash
    make integration-test
    ```

The tests cover all the layers of the application, focusing on unit tests for business logic in the domain layer and integration tests for the application layer.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
