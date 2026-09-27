# System Architecture

## 1. Architecture Overview

The Smart Hostel Management System follows a modular architecture. The main program acts as the central controller and connects different functional modules with the SQLite database.

## 2. System Architecture

```text
                    SMART HOSTEL MANAGEMENT SYSTEM
                                |
                                v
                           main.py
                                |
          +---------------------+---------------------+
          |          |           |          |          |
          v          v           v          v          v
      Student      Room        Fees    Complaints  Attendance
      Module      Module      Module      Module      Module
          |          |           |          |          |
          +----------+-----------+----------+----------+
                                |
                                v
                         Database Module
                         (database.py)
                                |
                                v
                         SQLite Database
                          (hostel.db)
                                |
                                v
                    Reports & Analytics Module
                           (reports.py)
```

## 3. Main Components

### main.py

Acts as the main controller of the application. It provides the main menu and connects all management modules.

### database.py

Handles the SQLite database connection and creates the required database tables.

### student.py

Manages student records, including adding, viewing, and searching students.

### room.py

Manages hostel room information.

### fees.py

Manages student fee records.

### complaints.py

Manages student complaints.

### attendance.py

Records student entry and exit attendance.

### reports.py

Generates basic reports related to students, rooms, and fees.

## 4. Database Layer

The system uses SQLite for persistent data storage.

The database file is:

```text
data/hostel.db
```

The main database tables are:

* students
* rooms
* fees
* complaints
* attendance

## 5. Architecture Flow

The general flow of the system is:

```text
User
  ↓
main.py
  ↓
Select Management Module
  ↓
Module Function
  ↓
Database Operation
  ↓
SQLite Database
  ↓
Result / Report
  ↓
User
```
