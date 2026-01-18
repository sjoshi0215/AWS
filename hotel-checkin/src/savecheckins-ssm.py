import json
import psycopg
import boto3

# Initialize SSM client
ssm_client = boto3.client('ssm')

def get_db_credentials():
    """Fetch database credentials from AWS Parameter Store"""
    try:
        db_host = ssm_client.get_parameter(Name='/hotel-checkin/db/host', WithDecryption=False)['Parameter']['Value']
        db_user = ssm_client.get_parameter(Name='/hotel-checkin/db/user', WithDecryption=False)['Parameter']['Value']
        db_pass = ssm_client.get_parameter(Name='/hotel-checkin/db/password', WithDecryption=True)['Parameter']['Value']
        return db_host, db_user, db_pass
    except Exception as e:
        raise Exception(f"Failed to retrieve database credentials from Parameter Store: {str(e)}")

def lambda_handler(event, context):
    body = json.loads(event["body"])
    
    db_host, db_user, db_pass = get_db_credentials()

    conn = psycopg.connect(
        host=db_host,
        dbname="hotel",
        user=db_user,
        password=db_pass,
        port=5432,
    )

    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO checkins
        (guest_name, email, booking_id, room_type, checkin_date)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            body["name"],
            body["email"],
            body["bookingId"],
            body["roomType"],
            body["checkinDate"],
        ),
    )

    conn.commit()
    cur.close()
    conn.close()

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Check-in saved"})
    }
