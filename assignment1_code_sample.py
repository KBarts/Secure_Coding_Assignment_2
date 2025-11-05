"""Assignment 2 sample script."""

import os
from urllib.request import urlopen
import pymysql


db_config = {"host": "mydatabase.com", "user": "admin", "password": "secret123"}


def get_user_input() -> str:
    """Prompt the user for a name and return it."""
    user_name = input("Enter your name: ")
    return user_name


def send_email(to: str, subject: str, body: str) -> None:
    """Send a simple email using a local mail program."""
    os.system(f'echo {body} | mail -s "{subject}" {to}')


def get_data() -> str:
    """Fetch text from a demo API and return it."""
    url = "http://insecure-api.com/get-data"
    with urlopen(url) as resp:
        text = resp.read().decode()
    return text


def save_to_db(text: str) -> None:
    """Insert provided data into the database."""
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{text}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    user_name = get_user_input()
    api_data = get_data()
    save_to_db(api_data)
    send_email("admin@example.com", "User Input", user_name)
