from modules.database import get_connection
from datetime import datetime


def mark_attendance():
    while True:
        try:
            student_id = int(input("Enter student ID: "))

            if student_id <= 0:
                print("Student ID must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid student ID.")

    print("\n1. Entry")
    print("2. Exit")

    choice = input("Enter attendance type: ")

    if choice == "1":
        entry_type = "Entry"
    elif choice == "2":
        entry_type = "Exit"
    else:
        print("Invalid attendance type.")
        return

    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT student_id FROM students WHERE student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("\nStudent not found. Please enter a valid student ID.")
        connection.close()
        return

    cursor.execute("""
        INSERT INTO attendance (student_id, entry_type, date_time)
        VALUES (?, ?, ?)
    """, (student_id, entry_type, date_time))

    connection.commit()
    connection.close()

    print("\nAttendance marked successfully!")


def view_attendance():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM attendance")
    records = cursor.fetchall()

    connection.close()

    if not records:
        print("\nNo attendance records found.")
        return

    print("\n========== ATTENDANCE RECORDS ==========")

    for record in records:
        print(f"""
Attendance ID : {record[0]}
Student ID    : {record[1]}
Type          : {record[2]}
Date & Time   : {record[3]}
-----------------------------------------
""")


def search_attendance():
    while True:
        try:
            student_id = int(input("Enter student ID: "))

            if student_id <= 0:
                print("Student ID must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid student ID.")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM attendance WHERE student_id = ?",
        (student_id,)
    )

    records = cursor.fetchall()
    connection.close()

    if records:
        print("\n========== STUDENT ATTENDANCE ==========")

        for record in records:
            print(f"""
Attendance ID : {record[0]}
Student ID    : {record[1]}
Type          : {record[2]}
Date & Time   : {record[3]}
-----------------------------------------
""")
    else:
        print("\nNo attendance record found.")


if __name__ == "__main__":
    print("\n========== ATTENDANCE MANAGEMENT ==========")
    print("1. Mark Attendance")
    print("2. View All Attendance")
    print("3. Search Student Attendance")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        view_attendance()
    elif choice == "3":
        search_attendance()
    else:
        print("Invalid choice.")