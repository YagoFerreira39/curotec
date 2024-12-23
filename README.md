# Curotec Test

This project is built using **FastAPI** and **Poetry**. It provides two endpoints: one for handling orders via a POST method and another for interacting with commodities through a WebSocket connection. The project is containerized using Docker and uses PostgreSQL as its database.

<p>
  <img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python">
  <img src="https://img.shields.io/badge/Witch--Doctor-1.2.0-blue" alt="Witch Doctor">
  <img src="https://img.shields.io/badge/Meeseeks--Singleton-0.4.4-blue" alt="Meeseeks Singleton">
  <img src="https://img.shields.io/badge/Loglifos-0.2.1-blue" alt="Loglifos">
  <img src="https://img.shields.io/badge/Pyfiglet-1.0.2-blue" alt="Pyfiglet">
  <img src="https://img.shields.io/badge/FastAPI-0.115.6-green" alt="FastAPI">
  <img src="https://img.shields.io/badge/Aiohttp-3.11.11-blue" alt="Aiohttp">
  <img src="https://img.shields.io/badge/Psycopg-3.1.10-yellow" alt="Psycopg">
  <img src="https://img.shields.io/badge/Psycopg--Pool-3.2.4-yellow" alt="Psycopg Pool">
  <img src="https://img.shields.io/badge/Uvicorn-0.34.0-green" alt="Uvicorn">
  <img src="https://img.shields.io/badge/Python--Decouple-3.8-blue" alt="Python Decouple">
</p>

## Project Architecture

This project was developed using **Clean Architecture** and adheres to **SOLID principles**, ensuring a scalable, maintainable, and testable codebase. The architecture is divided into distinct layers, each with a clear responsibility, promoting separation of concerns and minimizing dependencies between components.

### Layers Overview

1. **Adapters**:
   - **Purpose**: Acts as the interface between the external world and the application’s core.
   - **Components**:
     - **Controllers**: Handle incoming requests and map them to the appropriate use cases.
     - **Extensions**: Provide reusable functionalities or utilities.
     - **Repositories**: Abstract database operations, ensuring the domain layer is decoupled from the persistence layer.

2. **Domain**:
   - **Purpose**: Represents the core business logic and rules.
   - **Components**:
     - **Entities**: Define the fundamental objects of the domain, including their properties and behaviors.
     - **Models**: Provide data structures used across the domain layer.
     - **Enums**: Enumerations for constants that represent domain-specific options.

3. **Use Cases**:
   - **Purpose**: Contain the application’s specific business logic and orchestrate the flow of data between the domain and adapters.
   - **Components**:
     - **Use Cases**: Implement the core business rules and application workflows.
     - **Data Types**: Define the data structures required by use cases.

4. **Externals**:
   - **Purpose**: Handle interactions with external systems and frameworks.
   - **Components**:
     - **Infrastructures**: Manage external dependencies, such as database connections and message queues.
     - **Routers**: Define the API routes and bind them to the appropriate controllers.
     - **Services**: Integrate with external APIs and third-party services.

### Benefits of this Architecture

- **Scalability**: Easily add new features or layers without disrupting existing functionality.
- **Maintainability**: Well-organized code with clear responsibilities makes it easier to understand and update.
- **Testability**: Decoupled layers simplify unit testing and integration testing.
- **Flexibility**: Adapts to changes in requirements or technologies with minimal impact on the core logic.

This layered structure ensures the project is robust and ready for future enhancements or scaling requirements.


## Endpoints

### 1. **POST - /order/**
- **Description**: This endpoint allows users to execute an order for a specific commodity.
- **Path**: `/order/`
- **Method**: `POST`
- **Request Body**:
  - `user_id` (int): The ID of the user placing the order.
  - `commodity_name` (CommodityNameEnum): The name of the commodity being ordered.
  - `quantity` (int): The quantity of the commodity to order.
- **Response**:
  - **Success**:
    ```json
    {
      "status": true,
      "payload": {
        "name": "Gold",
        "unit_price": 1800.50,
        "order_amount": 54015.00,
        "quantity": 30,
        "order_id": "ORD12345"
      },
      "message": "",
      "error_code": 0
    }
    ```
  - **Error**:
    ```json
    {
      "status": false,
      "error_code": "INVALID_ORDER",
      "message": "Invalid order details provided"
    }
    ```

---

### 2. **WebSocket /commodity/ws**
- **Description**: This WebSocket endpoint allows real-time interaction with commodity data. Users can send a commodity name and receive its details, including price and last update time.
- **Path**: `/commodity/ws`
- **Method**: `WebSocket`
- **Workflow**:
  - The client sends a JSON payload with the commodity name.
  - The server responds with the details of the commodity.
- **Request Payload**:
  ```json
  {
    "commodity_name": "Gold"
  }
- **Response**:
- **Success**:
  ```json
    {
      "status": true,
      "payload": {
        "exchange": "NYSE",
        "name": "Gold",
        "price": 1800.50,
        "updated": 1695479400
      },
      "message": "",
      "error_code": 0
    }
    ```
- **Error**:
  ```json
  {
    "status": false,
    "error_code": "INVALID_ORDER",
    "message": "Invalid order details provided"
  }
  ```
# Running the Project

## Prerequisites
- **Docker**: Ensure Docker is installed on your system for containerized deployment.
- **Python 3.10 or higher**: Required for running the project locally.
- **Poetry**: Dependency management tool for Python projects.

## Clone the Repository
Start by cloning the repository to your local machine:
```bash
git clone https://github.com/YagoFerreira39/curotec
cd curotec
docker-compose build
docker-compose up
```
### Database Initialization

The project includes a `postgres-init.sql` file located in the `docker-entrypoint-initdb.d` folder. This file is automatically executed during the `docker-compose build` process. It initializes the PostgreSQL database by creating a table and inserting some fake data.

#### File: `docker-entrypoint-initdb.d/postgres-init.sql`

- **Creates a table**: Defines the structure of a table required for the project.
- **Inserts fake data**: Populates the table with sample data for testing purposes.

This ensures that the database is preconfigured with the necessary schema and data when the Docker container is built and started.

To customize the initialization or add more data, you can modify the `postgres-init.sql` file before running the `docker-compose build` command.
