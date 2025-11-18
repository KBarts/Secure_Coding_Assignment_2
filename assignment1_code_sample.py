"""Assignment 2 sample script."""

import pymysql
import requests


db_config = {"host": "mydatabase.com", "user": "admin", "password": "secret123"}


def get_user_input() -> str:
    """Prompt the user for a name and return it."""
    entered_name = input("Enter your name: ")
    return entered_name


def send_email(to: str, subject: str, body: str) -> None:
    """Simulate sending an email by printing it."""
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print()
    print(body)


def get_data() -> str:
    """Fetch text from a demo API and return it."""
    url = "https://secure-api.example.com/get-data"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.text


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
