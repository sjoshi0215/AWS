import json
import psycopg
import boto3

# Initialize SSM client
ssm_client = boto3.client('ssm')

def get_db_credentials():
    """Fetch database credentials from AWS Parameter Store"""
    try:
        db_host = ssm_client.get_parameter(Name='/hotel-checkin/db/host', WithDecryption=False)['Parameter']['Value']
        db_user = ssm_client.get_parameter(Name='/hotel-checkin/db/user', WithDecryption=True)['Parameter']['Value']
        db_pass = ssm_client.get_parameter(Name='/hotel-checkin/db/password', WithDecryption=True)['Parameter']['Value']
        return db_host, db_user, db_pass
    except Exception as e:
        raise Exception(f"Failed to retrieve database credentials from Parameter Store: {str(e)}")

def lambda_handler(event, context):
    db_host, db_user, db_pass = get_db_credentials()
    
    conn = psycopg.connect(
        host=db_host,
        dbname='hotel',
        user=db_user,
        password=db_pass,
        port=5432
    )

    cur = conn.cursor()
    cur.execute("""
        SELECT guest_name, email, booking_id, room_type, checkin_date
        FROM checkins
        ORDER BY created_at DESC
    """)

    rows = cur.fetchall()
    cur.close()
    conn.close()

    result = []
    for r in rows:
        result.append({
            "name": r[0],
            "email": r[1],
            "bookingId": r[2],
            "room": r[3],
            "date": str(r[4])
        })

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
