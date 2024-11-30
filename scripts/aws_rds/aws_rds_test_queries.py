#!/usr/bin/env python3
"""
aws_rds_test_queries.py

A script to verify that the AWS RDS MySQL database schema and seeding are correct
and to execute SQL queries from a file. It connects to the RDS database using
credentials stored in a .env file and prints the results of the queries.
"""

import os
import mysql.connector
from dotenv import load_dotenv


def load_environment_variables():
    """Load environment variables from the .env file."""
    dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
    if not os.path.exists(dotenv_path):
        print(f"Error: .env file not found at {dotenv_path}")
        exit(1)
    load_dotenv(dotenv_path)


def connect_to_database():
    """Establish a connection to the MySQL RDS database."""
    try:
        connection = mysql.connector.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT", "3306"),
            database=os.getenv("DB_NAME")
        )
        print("Connection to the AWS RDS database was successful!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def verify_schema_and_seeding(connection):
    """
    Verify that the schema and seeding were successfully performed.

    Args:
        connection (mysql.connector.connection.MySQLConnection): The database connection.
    """
    cursor = connection.cursor(dictionary=True)
    try:
        # Example queries to verify schema and data
        queries = [
            "SELECT COUNT(*) AS dam_count FROM dams;",
            "SELECT COUNT(*) AS latest_data_count FROM latest_data;",
            "SELECT COUNT(*) AS resource_count FROM dam_resources;"
        ]

        for index, query in enumerate(queries):
            print(f"\nVerifying with Query {index + 1}:\n{query}")
            cursor.execute(query)
            result = cursor.fetchone()
            print(f"Result: {result}")

    except mysql.connector.Error as err:
        print(f"Error while verifying schema and seeding: {err}")
    finally:
        cursor.close()


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
    """Main execution block to verify schema and execute SQL queries."""
    # Load environment variables
    load_environment_variables()

    # Connect to the database
    db_connection = connect_to_database()

    if db_connection:
        # Step 1: Verify schema and seeding
        print("Verifying schema and seeding...")
        verify_schema_and_seeding(db_connection)

        # Step 2: Execute queries from the SQL file
        sql_file_path = os.path.join(os.path.dirname(__file__), '../sql/example_queries.sql')
        print("\nExecuting example queries...")
        execute_queries(db_connection, sql_file_path)

        # Close the connection
        db_connection.close()
        print("Database connection closed.")


if __name__ == "__main__":
    main()
