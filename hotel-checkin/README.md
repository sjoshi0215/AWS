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
