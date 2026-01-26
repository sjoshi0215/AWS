


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
    
    
3) copilot to generate 3 microservices.
    order-service
    product-service
    user-service

4) Create 2 EC2 instances and upload the below microserive jars
    a) ec2-instance-user
            --> user-service-1.0.0.jar
    b) ec2-instance-product-order
            --> product-service-1.0.0.jar
            --> order-service-1.0.0.jar
    
    upload command using cmd -->  
    pscp -i <key_file>.ppk <file_name_to_upload> ec2-user@<ec2_ip_address>:/home/ec2-user/

5) In your EC2 instance run below command to download JDK 17 to run springboot microservices.
    command --> 
        sudo yum update -y
        sudo yum install java-17-amazon-corretto -y 
                    (Install Java 17 (Amazon Corretto – Recommended))

6) Attach the security group to the instance to accept HTTP request 

7) run all the 3 microservices
    java -jar <microservice_name>

8) Try to use below url to access your application.
        http://<ec2_instance_public_ip>:8001/api/v1/products/health
        http://<ec2_instance_public_ip>:8002/api/v1/users/health
        http://<ec2_instance_public_ip>:8003/api/v1/orders/health

9) If step 8 worked and able to access the application then we are good to create Application Load balancing

**************Application Load Balancing**************

1 EC2 Instance order service is running
2 EC2 Instance product/user service is running

10) Create target Group
    a) tg-products
        target-type : Instances
        Target Group Name : tg-products
        Protocol : http
        Port : 8001 (spring boot application is listening)
        health check : /api/v1/products/health
        Select instances from available instances
        Include as pending below
    
     b) tg-users
        target-type : Instances
        Target Group Name : tg-users
        Protocol : http
        Port : 8001 (spring boot application is listening)
        health check : /api/v1/users/health
        Select instances from available instances
        Include as pending below

    c) tg-orders
        target-type : Instances
        Target Group Name : tg-orders
        Protocol : http
        Port : 8003 (spring boot application is listening)
        health check : /api/v1/orders/health
        Select instances from available instances
        Include as pending below


11) Create ALB and associate the target group and add rules
    
        