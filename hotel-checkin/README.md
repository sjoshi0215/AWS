Backend   ---- Lambda function to persist to DB, 
Lambda trigger---API GATEWAY
DB       ----  RDS Postgres

![alt text](architecture.jpeg)

Step 1) Create S3 bucket 
        a) Allow public access
        b) After creating bucket GOTO bucket permission TAB to to provide permission.
                Allow bucket policy anonymous access: 
                {
                    "Version": "2012-10-17",		 	 	 
                    "Statement": [
                        {
                            "Sid": "PublicReadGetObject",
                            "Effect": "Allow",
                            "Principal": "*",
                            "Action": [
                                "s3:GetObject"
                            ],
                            "Resource": [
                                "arn:aws:s3:::Bucket-Name/*"
                            ]
                        }
                    ]
                } 

        c) GOTO bucket properties TAB where enable S3 static website
        d) Upload the html files in this bucket


Step 2) Creating RDS/Postgress DB steps
        a) Choose security group to enable incoming on port 5432 from anythwhere. This is require to setup to allow postgress incoming connection.
        b) Create a Postgres Database:
        c) Choose free tier: 
        d) username: postgres 
        e) pwd: Postgres1!
        f) Choose security group which we created in Step a.
        g) In Additional Configuration, disable Automated Backup

Step 3) Check the DB connection.
        a) Create a EC2 instance to connect to database
        b) Install postgresql clien on EC2: 
            sudo dnf update -y
            sudo dnf install postgresql15 -y
        c) psql -h hotel-checkin-db.ckpoyk4gmqrl.us-east-1.rds.amazonaws.com -U postgres -d hotel
        d) \dt to list tables

Step 4) Create table for our application in DB
        CREATE TABLE checkins (
                    id SERIAL PRIMARY KEY,
                    guest_name VARCHAR(100) NOT NULL,
                    email VARCHAR(150) NOT NULL,
                    booking_id VARCHAR(50) NOT NULL,
                    room_type VARCHAR(50),
                    checkin_date DATE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );



Step 5) Now create a lambada for savecheckin and list checkins
        a) In AWS console search for Lambda then create Function then   Provide below details.
            Function name -- save-checkin-lambda
            RUntime -- Python 3.12 
            Additional Configuration-
                Select default VPC (Attach the lambdas to a vpc because they need to access RDS)
                Select any Subnet 
                Security Group -- Selct default.
            Create Function
        
        b) In the code tab paste the savecheckins.py code
        c) In the Configuration TAB set the below property under environment
            DB_HOST : hotel-checkin-db.ckpoyk4gmqrl.us-east-1.rds.amazonaws.com
            DB_USER : postgres
            DB_PASS : Postgres1!
        d) In the python file we are using an external module psycopg to make a connection with DB. But that was not supported by AWS. SO make the programme run either you need to create your own layer (where you can create the layer with require module) or use the someone created layer. So will use the existing layer.
            For postgres module --> arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p312-psycopg:20
        e) Under Test TAB paste the below JSON and run
            {
                "body": "{\"name\": \"John Doe\", \"email\": \"john.doe@example.com\", \"bookingId\": \"BK123456\", \"roomType\": \"Deluxe Suite\", \"checkinDate\": \"2026-01-16\"}"
            }
            
            