# System Workflow

## 1. General Workflow

The Smart Hostel Management System follows a simple menu-driven workflow.

```text
START
  |
  v
Initialize Database
  |
  v
Display Main Menu
  |
  +-----------------------------+
  |                             |
  v                             v
Select Management Module      Exit
  |
  +--------+--------+--------+--------+--------+
  |        |        |        |        |        |
  v        v        v        v        v        v
Student   Room     Fees   Complaints Attendance Reports
  |        |        |        |        |        |
  +--------+--------+--------+--------+--------+
                         |
                         v
                  Perform Operation
                         |
                         v
                  Database Operation
                         |
                         v
                    Display Result
                         |
                         v
                    Return to Menu
```

## 2. Student Management Workflow

```text
Student Management
        |
        v
Select Add / View / Search
        |
        v
Enter Required Information
        |
        v
Validate Input
        |
        v
Store / Retrieve Data
        |
        v
Display Result
```

## 3. Room Management Workflow

```text
Room Management
       |
       v
Add / View / Search Room
       |
       v
Validate Room Information
       |
       v
Database Operation
       |
       v
Display Result
```

## 4. Fees Management Workflow

```text
Fees Management
       |
       v
Enter Student ID and Fee Amount
       |
       v
Validate Student ID
```
