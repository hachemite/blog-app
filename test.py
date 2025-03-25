import psycopg2
from urllib.parse import urlparse, quote_plus

def test_postgres_connection(database_url):
    try:
        # Parse the database URL
        parsed_url = urlparse(database_url)
        
        # Extract connection parameters
        connection_params = {
            'dbname': parsed_url.path.lstrip('/'),
            'user': parsed_url.username,
            'password': parsed_url.password,
            'host': parsed_url.hostname,
            'port': parsed_url.port or 5432
        }
        
        # Establish connection
        conn = psycopg2.connect(**connection_params)
        
        # Create a cursor to perform database operations
        cursor = conn.cursor()
        
        # Execute a simple query to test connection
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        
        print("Connection Successful!")
        print(f"PostgreSQL Database Version: {db_version[0]}")
        
        # Close cursor and connection
        cursor.close()
        conn.close()
        
    except psycopg2.Error as e:
        print(f"Database Connection Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Test the connection
database_url = 'postgresql://my_django_db_njjz_user:WIHu0Idev2kmxKgeMiAoijNrIkUSCPvw@dpg-cvhbsf1opnds73b34qdg-a/my_django_db_njjz'
test_postgres_connection(database_url)