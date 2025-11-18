"""Assignment 2 sample script."""

import os
import subprocess
from urllib.request import urlopen

import pymysql

DB_HOST = os.environ.get("DB_HOST", "mydatabase.com")
DB_USER = os.environ.get("DB_USER", "admin")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

db_config = {"host": DB_HOST, "user": DB_USER, "password": DB_PASSWORD}


def get_user_input() -> str:
    """Prompt the user for a name and return it."""
    entered_name = input("Enter your name: ")
    return entered_name


def send_email(to: str, subject: str, body: str) -> None:
    """Send a simple email using a local mail program."""
    subprocess.run(
        ["mail", "-s", subject, to],
        input=body.encode("utf-8"),
        check=True,
    )


def get_data() -> str:
    """Fetch text from a demo API and return it."""
    url = "https://insecure-api.com/get-data"
    with urlopen(url) as resp:
        text = resp.read().decode()
    return text


def save_to_db(text: str) -> None:
    """Insert provided data into the database."""
    query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    connection = pymysql.connect(**db_config)  # type: ignore[call-overload]
    cursor = connection.cursor()
    cursor.execute(query, (text, "Another Value"))
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    user_name = get_user_input()
    api_data = get_data()
    save_to_db(api_data)
    send_email("admin@example.com", "User Input", user_name)
