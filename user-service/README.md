# User Service

Spring Boot microservice for managing users.

## Running the Service

### Prerequisites
- Java 17 or higher
- Maven 3.6+

### Build and Run

```bash
cd user-service

# Build the project
mvn clean install

# Run the application
mvn spring-boot:run
```

The service will start on `http://localhost:8002`

### API Endpoints

- `POST /api/v1/users` - Create a new user
- `GET /api/v1/users` - Get all users
- `GET /api/v1/users/{userId}` - Get user by ID
- `PUT /api/v1/users/{userId}` - Update a user
- `DELETE /api/v1/users/{userId}` - Deactivate a user

### API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8002/swagger-ui.html`
- API Docs: `http://localhost:8002/v3/api-docs`

### Database

The service uses H2 in-memory database for development. Access the H2 console at:
`http://localhost:8002/h2-console`

Connection details:
- JDBC URL: `jdbc:h2:mem:userdb`
- Username: `sa`
- Password: (empty)
