from modules.database import get_connection


def student_report():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM rooms")
    total_rooms = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM complaints WHERE status = 'Pending'")
    pending_complaints = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM fees WHERE status = 'Pending'")
    pending_fees = cursor.fetchone()[0]

    connection.close()

    print("\n========== HOSTEL REPORT ==========")
    print(f"Total Students       : {total_students}")
    print(f"Total Rooms          : {total_rooms}")
    print(f"Pending Complaints   : {pending_complaints}")
    print(f"Pending Fee Records  : {pending_fees}")
    print("===================================")


def room_report():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT room_number, capacity, occupied
        FROM rooms
    """)

    rooms = cursor.fetchall()
    connection.close()

    if not rooms:
        print("\nNo room data available.")
        return

    print("\n========== ROOM OCCUPANCY REPORT ==========")

    for room in rooms:
        available = room[1] - room[2]

        print(f"""
Room Number : {room[0]}
Capacity    : {room[1]}
Occupied    : {room[2]}
Available   : {available}
--------------------------------------------
""")


def fee_report():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT SUM(amount)
        FROM fees
        WHERE status = 'Paid'
    """)

    paid_amount = cursor.fetchone()[0]

    cursor.execute("""
        SELECT SUM(amount)
        FROM fees
        WHERE status = 'Pending'
    """)

    pending_amount = cursor.fetchone()[0]

    connection.close()

    paid_amount = paid_amount if paid_amount else 0
    pending_amount = pending_amount if pending_amount else 0

    print("\n========== FEE REPORT ==========")
    print(f"Total Paid Amount    : ₹{paid_amount}")
    print(f"Total Pending Amount : ₹{pending_amount}")
    print("================================")


if __name__ == "__main__":
    print("\n========== HOSTEL REPORTS ==========")
    print("1. Student Report")
    print("2. Room Occupancy Report")
    print("3. Fee Report")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        student_report()
    elif choice == "2":
        room_report()
    elif choice == "3":
        fee_report()
    else:
        print("Invalid choice.")