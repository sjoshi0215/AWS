1) Microservices
    a) products
    b) users
    c) orders
   

2) Database - RDS schema
    a) PRODUCT SCHEMA
        TABLE --> PRODUCT

        CREATE SCHEMA IF NOT EXISTS product_schema;

        CREATE TABLE IF NOT EXISTS product_schema.product (
            product_id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            name                VARCHAR(255) NOT NULL,
            description         TEXT,
            price               NUMERIC(10,2) NOT NULL CHECK (price >= 0),
            currency            VARCHAR(3) NOT NULL,
            quantity_available  INTEGER NOT NULL CHECK (quantity_available >= 0),
            status              VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',
            created_at          TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            updated_at          TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );

        CREATE INDEX idx_product_name
            ON product_schema.product(name);

            INSERT STATEMENT

            INSERT INTO product_schema.product
                (product_id, name, description, price, currency, quantity_available, status)
            VALUES
                (
                    gen_random_uuid(),
                    'Donut',
                    'Freshly baked glazed donut',
                    2.50,
                    'USD',
                    100,
                    'ACTIVE'
                ),
                (
                    gen_random_uuid(),
                    'Cake',
                    'Chocolate layered cake',
                    15.00,
                    'USD',
                    50,
                    'ACTIVE'
    );






    b) USER SCHEMA
        TABLE --> USER TABLE

        CREATE SCHEMA IF NOT EXISTS user_schema;

        CREATE TABLE IF NOT EXISTS user_schema.app_user (
            user_id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            first_name      VARCHAR(100) NOT NULL,
            last_name       VARCHAR(100),
            email           VARCHAR(255) NOT NULL UNIQUE,
            password_hash   TEXT NOT NULL,
            phone           VARCHAR(20),
            status          VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',
            created_at      TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            updated_at      TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );

        CREATE INDEX idx_user_email
            ON user_schema.app_user(email);

    
    c) ORDER SCHEMA
        TABLE --> ORDER TABLE

        CREATE SCHEMA IF NOT EXISTS order_schema;

        CREATE TABLE IF NOT EXISTS order_schema.orders (
            order_id        UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            user_id         UUID NOT NULL,
            order_status    VARCHAR(30) NOT NULL DEFAULT 'CREATED',
            total_amount    NUMERIC(12,2) NOT NULL CHECK (total_amount >= 0),
            currency        VARCHAR(3) NOT NULL,
            created_at      TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            updated_at      TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );

        CREATE INDEX idx_order_user_id
            ON order_schema.orders(user_id);

        CREATE INDEX idx_order_status
            ON order_schema.orders(order_status);
    
    
3 APIs