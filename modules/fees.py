
from modules.database import get_connection


def add_fee():
    while True:
        try:
            student_id = int(input("Enter student ID: "))

            if student_id <= 0:
                print("Student ID must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid student ID.")

    while True:
        try:
            amount = float(input("Enter fee amount: "))

            if amount <= 0:
                print("Fee amount must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid amount.")

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
            INSERT INTO fees (student_id, amount)
            VALUES (?, ?)
        """, (student_id, amount))

        connection.commit()

        print("\nFee record added successfully!")

    except Exception as error:
        print(f"\nError: {error}")

    finally:
        connection.close()


def view_fees():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM fees")
    fees = cursor.fetchall()

    connection.close()

    if not fees:
        print("\nNo fee records found.")
        return

    print("\n========== FEE RECORDS ==========")

    for fee in fees:
        print(f"""
Fee ID        : {fee[0]}
Student ID    : {fee[1]}
Amount        : ₹{fee[2]}
Status        : {fee[3]}
Payment Date  : {fee[4]}
----------------------------------
""")


def search_fee():
    while True:
        try:
            student_id = int(input("Enter student ID to search fees: "))

            if student_id <= 0:
                print("Student ID must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid student ID.")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM fees WHERE student_id = ?",
        (student_id,)
    )

    fees = cursor.fetchall()

    connection.close()

    if fees:
        print("\n========== STUDENT FEE RECORDS ==========")

        for fee in fees:
            print(f"""
Fee ID        : {fee[0]}
Student ID    : {fee[1]}
Amount        : ₹{fee[2]}
Status        : {fee[3]}
Payment Date  : {fee[4]}
------------------------------------------
""")
    else:
        print("\nNo fee record found for this student.")


if __name__ == "__main__":
    print("\n========== FEES MANAGEMENT ==========")
    print("1. Add Fee")
    print("2. View All Fees")
    print("3. Search Student Fees")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_fee()
    elif choice == "2":
        view_fees()
    elif choice == "3":
        search_fee()
    else:
        print("Invalid choice.")

