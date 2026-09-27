from modules.database import get_connection


def add_student():
    name = input("Enter student name: ").strip()

    while True:
        try:
            age = int(input("Enter age: "))

            if age <= 0:
                print("Age must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number for age.")

    gender = input("Enter gender: ").strip()

    while True:
        phone = input("Enter phone number: ").strip()

        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("Please enter a valid 10-digit phone number.")

    course = input("Enter course: ").strip()

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO students (name, age, gender, phone, course)
            VALUES (?, ?, ?, ?, ?)
        """, (name, age, gender, phone, course))

        connection.commit()

        print("\nStudent added successfully!")

    except Exception as error:
        print(f"\nError: {error}")

    finally:
        connection.close()


def view_students():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    connection.close()

    if not students:
        print("\nNo student records found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for student in students:
        print(f"""
Student ID : {student[0]}
Name       : {student[1]}
Age        : {student[2]}
Gender     : {student[3]}
Phone      : {student[4]}
Course     : {student[5]}
Room ID    : {student[6]}
--------------------------------------
""")


def search_student():
    while True:
        try:
            student_id = int(input("Enter student ID to search: "))

            if student_id <= 0:
                print("Student ID must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid student ID.")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    connection.close()

    if student:
        print("\n========== STUDENT FOUND ==========")
        print(f"""
Student ID : {student[0]}
Name       : {student[1]}
Age        : {student[2]}
Gender     : {student[3]}
Phone      : {student[4]}
Course     : {student[5]}
Room ID    : {student[6]}
""")
    else:
        print("\nStudent not found.")


if __name__ == "__main__":
    print("\n========== STUDENT MANAGEMENT ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    else:
        print("Invalid choice.")