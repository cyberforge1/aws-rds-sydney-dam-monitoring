#!/usr/bin/env python3
"""
local_run_queries.py

A script to execute SQL queries from a file on a local MySQL database.
It connects to the database using credentials stored in a .env file and
executes the SQL commands, printing the results.
"""

import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve database configuration from environment variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "3306")  # Default to 3306 if not set


def connect_to_database():
    """Establish a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        print("Connection to the database was successful!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def execute_queries(connection, sql_file_path):
    """
    Execute SQL queries from a file and print the results.

    Args:
        connection (mysql.connector.connection.MySQLConnection): The database connection.
        sql_file_path (str): The path to the SQL file containing queries.
    """
    cursor = connection.cursor(dictionary=True)  # Use dictionary=True to get results as dict
    try:
        # Open and read the SQL file
        with open(sql_file_path, 'r') as file:
            sql_script = file.read()

        # Split the SQL script into individual queries
        sql_queries = sql_script.split(';')

        # Execute each query and print results
        for index, query in enumerate(sql_queries):
            if query.strip():  # Skip empty or whitespace-only queries
                print(f"\nExecuting Query {index + 1}:\n{query.strip()}")
                cursor.execute(query)
                results = cursor.fetchall()

                print(f"Results for Query {index + 1}:")
                if results:
                    for row in results:
                        print(row)
                else:
                    print("No results found.")

    except FileNotFoundError:
        print(f"Error: The file {sql_file_path} does not exist.")
    except mysql.connector.Error as err:
        print(f"Error while executing queries: {err}")
    finally:
        cursor.close()


def main():
    """Main execution block to execute SQL queries."""
    # Connect to the database
    db_connection = connect_to_database()

    if db_connection:
        # Define the path to the SQL file
        sql_file_path = "sql/example_queries.sql"  # Ensure this path is correct

        # Execute queries and print the results
        execute_queries(db_connection, sql_file_path)

        # Close the connection
        db_connection.close()
        print("Database connection closed.")


if __name__ == "__main__":
    main()
