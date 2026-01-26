# Product Service

Spring Boot microservice for managing products.

## Running the Service

### Prerequisites
- Java 17 or higher
- Maven 3.6+

### Build and Run

```bash
cd product-service

# Build the project
mvn clean install

# Run the application
mvn spring-boot:run
```

The service will start on `http://localhost:8001`

### API Endpoints

- `POST /api/v1/products` - Create a new product
- `GET /api/v1/products` - Get all products
- `GET /api/v1/products/{productId}` - Get product by ID
- `PUT /api/v1/products/{productId}` - Update a product
- `DELETE /api/v1/products/{productId}` - Delete a product

### API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8001/swagger-ui.html`
- API Docs: `http://localhost:8001/v3/api-docs`

### Database

The service uses H2 in-memory database for development. Access the H2 console at:
`http://localhost:8001/h2-console`

Connection details:
- JDBC URL: `jdbc:h2:mem:productdb`
- Username: `sa`
- Password: (empty)
