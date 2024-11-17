Here’s a `README.md` template for your services: `payment_service`, `product_service`, `user_service`, and `order_service`. You can customize it further as per your project specifics.

---

# Microservices for E-Commerce Application

This repository contains the microservices for the E-Commerce application. Each service is built using FastAPI and includes features such as handling requests, database operations, and inter-service communication.

## Table of Contents
- [Overview](#overview)
- [Services](#services)
  - [Payment Service](#payment-service)
  - [Product Service](#product-service)
  - [User Service](#user-service)
  - [Order Service](#order-service)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Running the Services](#running-the-services)

---

## Overview
This e-commerce application uses a microservices architecture where each service is responsible for a specific domain:
- **Payment Service**: Manages payment processing.
- **Product Service**: Handles product-related operations.
- **User Service**: Manages user data.
- **Order Service**: Handles order creation, updates, and cancellations.

Each service uses SQLAlchemy for database operations and can be deployed locally using Docker.

---

## Services

### Payment Service
**Description**: Processes payments for orders.

**Features**:
- Accepts payment requests.
- Validates payment details.
- Records payment status (success/failure).

**Endpoints**:
- `POST /payments/`: Process a payment.
- `GET /payments/{order_id}`: Get payment status by order ID.

---

### Product Service
**Description**: Manages products and their stock.

**Features**:
- CRUD operations for products.
- Stock reservation for orders.

**Endpoints**:
- `POST /products/`: Create a new product.
- `GET /products/{product_id}`: Retrieve product details.
- `PUT /products/reserve`: Reserve stock for an order.

---

### User Service
**Description**: Handles user registration and authentication.

**Features**:
- Register new users.
- Authenticate users.

**Endpoints**:
- `POST /users/`: Register a new user.
- `POST /login/`: Authenticate a user.
-  `PUT /profile/`: Update Profile,

---

### Order Service
**Description**: Manages order lifecycle.

**Features**:
- Create, update, and cancel orders.
- Communicates with Payment and Product services for payment and stock validation.

**Endpoints**:
- `POST /orders/`: Create a new order.
- `GET /orders/{order_id}`: Retrieve order details.
- `PUT /orders/{order_id}`: Update an existing order.
- `DELETE /orders/{order_id}`: Cancel an order.

---

## Prerequisites
Ensure you have the following installed:
- Python 3.10+
- Docker
- Postman (optional, for API testing)
- Postgress

---

## Setup and Installation

### Clone the Repository
```bash
git clone https://github.com/your-repo/ecommerce-microservices.git
cd ecommerce-microservices
```

### Install Dependencies
For each service:
1. Navigate to the service directory:
   ```bash
   cd payment_service  # Replace with product_service, user_service, order_service
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Setup Databases
Ensure PostgreSQL is running for all services. Update database connection strings in `database.py` for each service.

---

## Running the Services

### Using Docker
1. Build the Docker images:
   ```bash
   docker-compose build
   ```
2. Start the services:
   ```bash
   docker-compose up
   ```

### Manually
Run each service in a separate terminal:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000  # Replace with different ports for each service
```

---

## API Documentation
Each service provides interactive API documentation powered by Swagger:
- **Payment Service**: `http://localhost:8000/docs`
- **Product Service**: `http://localhost:8001/docs`
- **User Service**: `http://localhost:8002/docs`
- **Order Service**: `http://localhost:8003/docs`

You can test APIs directly through these interfaces.

---

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

