# E-Commerce Microservices

A complete Spring Boot microservices architecture with three independent services: Product, User, and Order services.

## Architecture Overview

This project implements three microservices:

1. **Product Service** (Port 8001)
   - Manages product catalog
   - CRUD operations for products
   - Product inventory management

2. **User Service** (Port 8002)
   - Manages user accounts
   - CRUD operations for users
   - User profile management

3. **Order Service** (Port 8003)
   - Manages customer orders
   - Order creation and tracking
   - Order-item management

## Project Structure

```
microservices/
├── product-service/
│   ├── src/main/java/com/microservices/product/
│   │   ├── controller/
│   │   ├── service/
│   │   ├── entity/
│   │   ├── dto/
│   │   ├── repository/
│   │   └── ProductServiceApplication.java
│   ├── pom.xml
│   └── README.md
├── user-service/
│   ├── src/main/java/com/microservices/user/
│   │   ├── controller/
│   │   ├── service/
│   │   ├── entity/
│   │   ├── dto/
│   │   ├── repository/
│   │   └── UserServiceApplication.java
│   ├── pom.xml
│   └── README.md
├── order-service/
│   ├── src/main/java/com/microservices/order/
│   │   ├── controller/
│   │   ├── service/
│   │   ├── entity/
│   │   ├── dto/
│   │   ├── repository/
│   │   └── OrderServiceApplication.java
│   ├── pom.xml
│   └── README.md
├── pom.xml (parent)
└── README.md
```

## Prerequisites

- Java 17 or higher
- Maven 3.6 or higher

## Quick Start

### Build All Services

```bash
mvn clean install
```

### Run Individual Services

**Product Service:**
```bash
cd product-service
mvn spring-boot:run
```

**User Service:**
```bash
cd user-service
mvn spring-boot:run
```

**Order Service:**
```bash
cd order-service
mvn spring-boot:run
```

## API Endpoints

### Product Service (http://localhost:8001/api/v1)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/products` | Create product |
| GET | `/products` | Get all products |
| GET | `/products/{productId}` | Get product by ID |
| PUT | `/products/{productId}` | Update product |
| DELETE | `/products/{productId}` | Delete product |

### User Service (http://localhost:8002/api/v1)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/users` | Create user |
| GET | `/users` | Get all users |
| GET | `/users/{userId}` | Get user by ID |
| PUT | `/users/{userId}` | Update user |
| DELETE | `/users/{userId}` | Deactivate user |

### Order Service (http://localhost:8003/api/v1)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/orders` | Create order |
| GET | `/orders` | Get all orders |
| GET | `/orders/{orderId}` | Get order by ID |
| GET | `/orders/user/{userId}` | Get orders by user ID |

## Technologies Used

- **Spring Boot 3.2.0** - Application framework
- **Spring Data JPA** - Data access layer
- **H2 Database** - In-memory database (development)
- **Lombok** - Reduce boilerplate code
- **SpringDoc OpenAPI** - API documentation (Swagger)

## Development Notes

### Database Configuration

Each service uses H2 in-memory database for development. To persist data, you can:

1. Change the database URL from `jdbc:h2:mem:` to `jdbc:h2:./data/`
2. Switch to PostgreSQL or MySQL by updating:
   - `application.yml` datasource properties
   - `pom.xml` dependencies

### API Documentation

Each service provides Swagger UI documentation:
- Product: http://localhost:8001/swagger-ui.html
- User: http://localhost:8002/swagger-ui.html
- Order: http://localhost:8003/swagger-ui.html

### H2 Database Console

Access H2 console for each service:
- Product: http://localhost:8001/h2-console
- User: http://localhost:8002/h2-console
- Order: http://localhost:8003/h2-console

## Future Enhancements

- [ ] Add inter-service communication (REST client/Feign)
- [ ] Implement service discovery (Eureka)
- [ ] Add API Gateway (Spring Cloud Gateway)
- [ ] Implement distributed tracing (Sleuth + Zipkin)
- [ ] Add circuit breaker pattern (Resilience4j)
- [ ] Database persistence (PostgreSQL/MySQL)
- [ ] Docker containerization
- [ ] Kubernetes deployment manifests
- [ ] Unit and integration tests

## License

MIT License
