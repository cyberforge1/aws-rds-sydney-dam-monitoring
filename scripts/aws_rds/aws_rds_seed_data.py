#!/usr/bin/env python3
"""
aws_rds_seed_data.py

A script to seed an AWS RDS MySQL database using an SQL file.
It connects to the RDS database using credentials stored in a .env file
and executes the SQL commands to populate the database with example data.
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
    # Load environment variables
    load_environment_variables()

    # Connect to the database
    db_connection = connect_to_database()

    if db_connection:
        # Define the path to the SQL file
        sql_file_path = os.path.join(os.path.dirname(__file__), '../sql/example_data.sql')

        # Seed the database using the SQL file
        seed_database_from_file(db_connection, sql_file_path)

        # Close the connection
        db_connection.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()
