import mysql.connector
from mysql.connector import Error

def connect():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            database="datalogger",
            user="root",
            password="root"
        )
        return connection
    except Error as e:
        print("Error:", e)
        return None

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        return True
    except Error as e:
        print("Error:", e)
        return False
