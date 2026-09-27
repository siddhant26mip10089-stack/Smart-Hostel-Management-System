from modules.database import get_connection
from datetime import datetime


def add_complaint():
    while True:
        try:
            student_id = int(input("Enter student ID: "))

            if student_id <= 0:
                print("Student ID must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid student ID.")

    complaint = input("Enter complaint: ").strip()

    if not complaint:
        print("Complaint cannot be empty.")
        return

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "SELECT student_id FROM students WHERE student_id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        if not student:
            print("\nStudent not found. Please enter a valid student ID.")
            return

        cursor.execute("""
            INSERT INTO complaints (student_id, complaint, created_at)
            VALUES (?, ?, ?)
        """, (student_id, complaint, created_at))

        connection.commit()

        print("\nComplaint submitted successfully!")

    except Exception as error:
        print(f"\nError: {error}")

    finally:
        connection.close()


def view_complaints():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM complaints")
    complaints = cursor.fetchall()

    connection.close()

    if not complaints:
        print("\nNo complaints found.")
        return

    print("\n========== COMPLAINT LIST ==========")

    for complaint in complaints:
        print(f"""
Complaint ID : {complaint[0]}
Student ID   : {complaint[1]}
Complaint    : {complaint[2]}
Status       : {complaint[3]}
Created At   : {complaint[4]}
-------------------------------------
""")


def search_complaint():
    while True:
        try:
            student_id = int(input("Enter student ID to search complaints: "))

            if student_id <= 0:
                print("Student ID must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid student ID.")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM complaints WHERE student_id = ?",
        (student_id,)
    )

    complaints = cursor.fetchall()
    connection.close()

    if complaints:
        print("\n========== STUDENT COMPLAINTS ==========")

        for complaint in complaints:
            print(f"""
Complaint ID : {complaint[0]}
Student ID   : {complaint[1]}
Complaint    : {complaint[2]}
Status       : {complaint[3]}
Created At   : {complaint[4]}
-----------------------------------------
""")
    else:
        print("\nNo complaints found for this student.")


if __name__ == "__main__":
    print("\n========== COMPLAINT MANAGEMENT ==========")
    print("1. Add Complaint")
    print("2. View All Complaints")
    print("3. Search Student Complaints")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_complaint()
    elif choice == "2":
        view_complaints()
    elif choice == "3":
        search_complaint()
    else:
        print("Invalid choice.")