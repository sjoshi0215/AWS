# PostgreSQL Database Configuration

All three microservices have been configured to use PostgreSQL on AWS RDS.

## Database Connection Details

- **Host**: postgress-db.ckpoyk4gmqrl.us-east-1.rds.amazonaws.com
- **Port**: 5432 (default)
- **Database**: cafe
- **Username**: postgres
- **Password**: Set via environment variable `DB_PASSWORD`

## Configuration in Each Service

All three services' `application.yml` files have been updated with:

```yaml
spring:
  datasource:
    url: jdbc:postgresql://postgress-db.ckpoyk4gmqrl.us-east-1.rds.amazonaws.com:5432/cafe
    driver-class-name: org.postgresql.Driver
    username: postgres
    password: ${DB_PASSWORD}
  jpa:
    database-platform: org.hibernate.dialect.PostgreSQLDialect
    hibernate:
      ddl-auto: update
```

## Running the Services

Before running any service, set the database password environment variable:

### On Linux/Mac:
```bash
export DB_PASSWORD=your_postgres_password
```

### On Windows (PowerShell):
```powershell
$env:DB_PASSWORD="your_postgres_password"
```

### Then build and run:
```bash
mvn clean install
mvn spring-boot:run
```

## Alternative: Using application-prod.yml

You can also create separate profiles for different environments:

### Create `application-prod.yml`:
```yaml
spring:
  datasource:
    url: jdbc:postgresql://postgress-db.ckpoyk4gmqrl.us-east-1.rds.amazonaws.com:5432/cafe
    driver-class-name: org.postgresql.Driver
    username: postgres
    password: ${DB_PASSWORD}
  jpa:
    database-platform: org.hibernate.dialect.PostgreSQLDialect
    hibernate:
      ddl-auto: validate
    show-sql: false
```

### Run with the profile:
```bash
mvn spring-boot:run -Dspring.profiles.active=prod
```

## Database Schema Auto-Creation

The services are configured with `ddl-auto: update` which will:
- Automatically create tables on first run if they don't exist
- Update existing tables if entity definitions change
- Never drop tables or data

For production, consider changing to `validate` to prevent unwanted schema changes.

## Verification

To verify the connection is working:

1. Check the application logs for connection messages
2. Query the database directly using a PostgreSQL client:
```bash
psql -h postgress-db.ckpoyk4gmqrl.us-east-1.rds.amazonaws.com -U postgres -d cafe
```

3. Or connect using pgAdmin or DBeaver (GUI tools)

## Troubleshooting

**Connection Refused**: 
- Verify the RDS security group allows inbound traffic on port 5432
- Check that DB_PASSWORD environment variable is set correctly
- Ensure the RDS instance is available

**Authentication Failed**:
- Confirm username and password are correct
- Verify the user has access to the 'cafe' database

**Database Not Found**:
- Ensure the 'cafe' database exists in PostgreSQL
- If not, create it:
```sql
CREATE DATABASE cafe;
```
