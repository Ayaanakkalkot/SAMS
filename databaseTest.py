import mysql.connector
from mysql.connector import Error

def fetch_databases():
    try:
        # Establish the connection
        conn = mysql.connector.connect(
            host='localhost', 
            username='root', 
            password='ayaan786', 
            database='face_recognition', 
            port=3306
        )
        
        if conn.is_connected():
            print("Successfully connected to the database!")

            # Create a cursor and execute the query
            cursor = conn.cursor()
            cursor.execute("SHOW DATABASES")
            
            # Fetch all databases
            databases = cursor.fetchall()
            print("Databases available:")
            for db in databases:
                print(f"- {db[0]}")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close the connection
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("MySQL connection closed.")

# Call the function
fetch_databases()
