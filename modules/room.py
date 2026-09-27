
from modules.database import get_connection


def add_room():
    room_number = input("Enter room number: ").strip()

    while True:
        try:
            capacity = int(input("Enter room capacity: "))

            if capacity <= 0:
                print("Capacity must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number for capacity.")

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO rooms (room_number, capacity)
            VALUES (?, ?)
        """, (room_number, capacity))

        connection.commit()

        print("\nRoom added successfully!")

    except Exception as error:
        print(f"\nError: {error}")

    finally:
        connection.close()


def view_rooms():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM rooms")
    rooms = cursor.fetchall()

    connection.close()

    if not rooms:
        print("\nNo room records found.")
        return

    print("\n========== ROOM RECORDS ==========")

    for room in rooms:
        print(f"""
Room ID     : {room[0]}
Room Number : {room[1]}
Capacity    : {room[2]}
Occupied    : {room[3]}
-----------------------------------
""")


def search_room():
    while True:
        try:
            room_id = int(input("Enter room ID to search: "))

            if room_id <= 0:
                print("Room ID must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid room ID.")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM rooms WHERE room_id = ?",
        (room_id,)
    )

    room = cursor.fetchone()

    connection.close()

    if room:
        print("\n========== ROOM FOUND ==========")
        print(f"""
Room ID     : {room[0]}
Room Number : {room[1]}
Capacity    : {room[2]}
Occupied    : {room[3]}
""")
    else:
        print("\nRoom not found.")


if __name__ == "__main__":
    print("\n========== ROOM MANAGEMENT ==========")
    print("1. Add Room")
    print("2. View Rooms")
    print("3. Search Room")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_room()
    elif choice == "2":
        view_rooms()
    elif choice == "3":
        search_room()
    else:
        print("Invalid choice.")

