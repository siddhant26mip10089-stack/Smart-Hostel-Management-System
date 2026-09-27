
import sqlite3

DATABASE_NAME = "data/hostel.db"


def test_database_connection():
    connection = sqlite3.connect(DATABASE_NAME)

    assert connection is not None

    connection.close()


def test_required_tables():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table'
    """)

    tables = [row[0] for row in cursor.fetchall()]

    required_tables = [
        "students",
        "rooms",
        "fees",
        "complaints",
        "attendance"
    ]

    for table in required_tables:
        assert table in tables

    connection.close()


if __name__ == "__main__":
    test_database_connection()
    test_required_tables()
    print("All tests passed successfully!")

