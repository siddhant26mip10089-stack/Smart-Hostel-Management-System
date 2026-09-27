# Database Design

## 1. Database Overview

The Smart Hostel Management System uses an SQLite database to store hostel-related information permanently.

Database file:

```text
data/hostel.db
```

## 2. Database Tables

The system contains five main tables.

### 2.1 Students Table

| Field      | Data Type | Description          |
| ---------- | --------- | -------------------- |
| student_id | INTEGER   | Unique student ID    |
| name       | TEXT      | Student name         |
| age        | INTEGER   | Student age          |
| gender     | TEXT      | Student gender       |
| phone      | TEXT      | Student phone number |
| course     | TEXT      | Student course       |
| room_id    | INTEGER   | Assigned room ID     |

### 2.2 Rooms Table

| Field       | Data Type | Description               |
| ----------- | --------- | ------------------------- |
| room_id     | INTEGER   | Unique room ID            |
| room_number | TEXT      | Room number               |
| capacity    | INTEGER   | Maximum room capacity     |
| occupied    | INTEGER   | Number of occupied places |

### 2.3 Fees Table

| Field        | Data Type | Description        |
| ------------ | --------- | ------------------ |
| fee_id       | INTEGER   | Unique fee ID      |
| student_id   | INTEGER   | Related student ID |
| amount       | REAL      | Fee amount         |
| status       | TEXT      | Payment status     |
| payment_date | TEXT      | Date of payment    |

### 2.4 Complaints Table

| Field        | Data Type | Description                      |
| ------------ | --------- | -------------------------------- |
| complaint_id | INTEGER   | Unique complaint ID              |
| student_id   | INTEGER   | Related student ID               |
| complaint    | TEXT      | Complaint description            |
| status       | TEXT      | Complaint status                 |
| created_at   | TEXT      | Complaint creation date and time |

### 2.5 Attendance Table

| Field         | Data Type | Description              |
| ------------- | --------- | ------------------------ |
| attendance_id | INTEGER   | Unique attendance ID     |
| student_id    | INTEGER   | Related student ID       |
| entry_type    | TEXT      | Entry or Exit            |
| date_time     | TEXT      | Attendance date and time |

## 3. Database Relationship

```text
                    STUDENTS
                       |
          +------------+------------+
          |            |            |
          v            v            v
        FEES      COMPLAINTS    ATTENDANCE

                    STUDENTS
                       |
                       v
                    ROOMS
```

The `student_id` field connects student records with fee, complaint, and attendance records.

The `room_id` field can be used to associate a student with a hostel room.

## 4. Database Operations

The system performs the following basic database operations:

* INSERT — Add new records
* SELECT — View and search records
* CREATE TABLE — Create required tables
* UPDATE-ready structure — Status and other fields can support future updates

## 5. Database Advantages

SQLite was selected because:

* It is lightweight.
* It does not require a separate database server.
* It stores data permanently in a local database file.
* It is suitable for a small academic management application.
