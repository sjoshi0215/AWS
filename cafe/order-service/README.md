# Order Service

Spring Boot microservice for managing orders.

## Running the Service

### Prerequisites
- Java 17 or higher
- Maven 3.6+

### Build and Run

```bash
cd order-service

# Build the project
mvn clean install

# Run the application
mvn spring-boot:run
```

The service will start on `http://localhost:8003`

### API Endpoints

- `POST /api/v1/orders` - Create a new order
- `GET /api/v1/orders` - Get all orders
- `GET /api/v1/orders/{orderId}` - Get order by ID
- `GET /api/v1/orders/user/{userId}` - Get orders by user ID

### API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8003/swagger-ui.html`
- API Docs: `http://localhost:8003/v3/api-docs`

### Database

The service uses H2 in-memory database for development. Access the H2 console at:
`http://localhost:8003/h2-console`

Connection details:
- JDBC URL: `jdbc:h2:mem:orderdb`
- Username: `sa`
- Password: (empty)
