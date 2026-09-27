from modules.database import create_tables
from modules.student import add_student, view_students, search_student
from modules.room import add_room, view_rooms, search_room
from modules.fees import add_fee, view_fees, search_fee
from modules.complaints import add_complaint, view_complaints, search_complaint
from modules.attendance import mark_attendance, view_attendance, search_attendance
from modules.reports import student_report, room_report, fee_report


def student_menu():
    while True:
        print("\n========== STUDENT MANAGEMENT ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def room_menu():
    while True:
        print("\n========== ROOM MANAGEMENT ==========")
        print("1. Add Room")
        print("2. View Rooms")
        print("3. Search Room")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_room()
        elif choice == "2":
            view_rooms()
        elif choice == "3":
            search_room()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def fee_menu():
    while True:
        print("\n========== FEES MANAGEMENT ==========")
        print("1. Add Fee")
        print("2. View Fees")
        print("3. Search Student Fees")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_fee()
        elif choice == "2":
            view_fees()
        elif choice == "3":
            search_fee()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def complaint_menu():
    while True:
        print("\n========== COMPLAINT MANAGEMENT ==========")
        print("1. Add Complaint")
        print("2. View Complaints")
        print("3. Search Student Complaints")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_complaint()
        elif choice == "2":
            view_complaints()
        elif choice == "3":
            search_complaint()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def attendance_menu():
    while True:
        print("\n========== ATTENDANCE MANAGEMENT ==========")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Search Student Attendance")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            search_attendance()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def reports_menu():
    while True:
        print("\n========== REPORTS & ANALYTICS ==========")
        print("1. Student Report")
        print("2. Room Occupancy Report")
        print("3. Fee Report")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            student_report()
        elif choice == "2":
            room_report()
        elif choice == "3":
            fee_report()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def main():
    create_tables()

    while True:
        print("\n")
        print("==============================================")
        print("       SMART HOSTEL MANAGEMENT SYSTEM")
        print("==============================================")
        print("1. Student Management")
        print("2. Room Management")
        print("3. Fees Management")
        print("4. Complaint Management")
        print("5. Attendance Management")
        print("6. Reports & Analytics")
        print("7. Exit")
        print("==============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            room_menu()
        elif choice == "3":
            fee_menu()
        elif choice == "4":
            complaint_menu()
        elif choice == "5":
            attendance_menu()
        elif choice == "6":
            reports_menu()
        elif choice == "7":
            print("\nThank you for using Smart Hostel Management System!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()