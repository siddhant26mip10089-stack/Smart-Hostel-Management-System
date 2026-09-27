# Smart Hostel Management System

## Overview

Smart Hostel Management System is a Python-based application developed to manage common hostel operations in a simple and organized way.

The system uses SQLite for storing student, room, fee, complaint, and attendance records.

## Features

* Student Management
* Room Management
* Fees Management
* Complaint Management
* Attendance Management
* Reports and Analytics
* SQLite Database
* Input Validation and Error Handling

## Technologies Used

* Python 3
* SQLite
* Visual Studio Code
* Git
* GitHub

## Project Structure

```text
Smart-Hostel-Management-System/
│
├── main.py
├── README.md
├── statement.md
│
├── data/
│   └── hostel.db
│
├── modules/
│   ├── __init__.py
│   ├── database.py
│   ├── student.py
│   ├── room.py
│   ├── fees.py
│   ├── complaints.py
│   ├── attendance.py
│   └── reports.py
│
├── reports/
├── tests/
│
└── docs/
    ├── requirements.md
    ├── architecture.md
    ├── workflow.md
    ├── database.md
    └── testing.md
```

## Requirements

* Python 3.x
* Visual Studio Code or another Python-compatible IDE
* No external database server is required because the project uses SQLite.

## How to Run

### 1. Clone or download the project

Open the project folder in Visual Studio Code.

### 2. Open the terminal

Navigate to the project root folder.

### 3. Run the application

```bash
python main.py
```

### 4. Use the Main Menu

The application provides the following options:

1. Student Management
2. Room Management
3. Fees Management
4. Complaint Management
5. Attendance Management
6. Reports & Analytics
7. Exit

## Database

The project uses SQLite.

Database file:

```text
data/hostel.db
```

The database contains tables for:

* Students
* Rooms
* Fees
* Complaints
* Attendance

## Testing

The major modules were tested using valid and invalid inputs.

Testing includes:

* Student record operations
* Room operations
* Fee operations
* Complaint operations
* Attendance operations
* Report generation
* Input validation
* Database operations

Detailed testing information is available in:

```text
docs/testing.md
```

## Documentation

Additional project documentation is available in the `docs` folder:

* `requirements.md`
* `architecture.md`
* `workflow.md`
* `database.md`
* `testing.md`

## Future Enhancements

Possible future improvements include:

* Login and authentication
* Automatic room allocation
* Fee payment tracking
* Improved graphical user interface
* Exporting reports to PDF or Excel

## Author

Smart Hostel Management System
Academic Project
