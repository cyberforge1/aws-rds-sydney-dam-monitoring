#!/usr/bin/env python3
"""
local_db_seeding.py

A script to seed a local MySQL database using an SQL file. It connects to the database
using credentials stored in a .env file and executes the SQL commands to populate the database.
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

def seed_database_from_file(connection, sql_file_path):
    """
    Seed the database using an SQL file.

    Args:
        connection (mysql.connector.connection.MySQLConnection): The database connection.
        sql_file_path (str): The path to the SQL file containing seed data.
    """
    cursor = connection.cursor()
    try:
        # Open and read the SQL file
        with open(sql_file_path, 'r') as file:
            sql_script = file.read()

        # Split the SQL script into individual statements
        sql_commands = sql_script.split(';')
        for command in sql_commands:
            # Skip empty or whitespace-only commands
            if command.strip():
                cursor.execute(command)
        
        # Commit the changes to the database
        connection.commit()
        print(f"Data from {sql_file_path} has been seeded into the database successfully!")

    except FileNotFoundError:
        print(f"Error: The file {sql_file_path} does not exist.")
    except mysql.connector.Error as err:
        print(f"Error while seeding data: {err}")
    finally:
        cursor.close()

def main():
    """Main execution block to seed the database."""
    # Connect to the database
    db_connection = connect_to_database()

    if db_connection:
        # Define the path to the SQL file
        sql_file_path = "sql/example_data.sql"  # Ensure this path is correct

        # Seed the database using the SQL file
        seed_database_from_file(db_connection, sql_file_path)

        # Close the connection
        db_connection.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()
