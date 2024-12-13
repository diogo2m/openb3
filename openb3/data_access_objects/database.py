import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.connection = None

    def execute_query(self, query, params=None):
        cursor = None
        try:
            cursor = self.connection.cursor(dictionary=True, buffered=True)
            cursor.execute(query, params)

            if not query.strip().lower().startswith("select"):
                self.connection.commit()

            return cursor
        except Error as e:
            print(f"Error executing query: {e}")
            if cursor:
                cursor.close()
            return None

    def fetch_all(self, query, params=None):
        cursor = None
        try:
            cursor = self.execute_query(query, params)
            if cursor:
                result = cursor.fetchall()
                return result
        except Error as e:
            print(f"Error fetching all results: {e}")
        finally:
            if cursor:
                cursor.close()
        return []

    def fetch_one(self, query, params=None):
        cursor = None
        try:
            cursor = self.execute_query(query, params)
            if cursor:
                result = cursor.fetchone()
                return result
        except Error as e:
            print(f"Error fetching one result: {e}")
        finally:
            if cursor:
                cursor.close()
        return None

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")
