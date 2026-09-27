# Testing Documentation

## 1. Testing Overview

The Smart Hostel Management System was tested by running the different modules and checking whether the expected output was produced for valid and invalid inputs.

## 2. Test Cases

| Test Case      | Input / Action                 | Expected Result                  | Status |
| -------------- | ------------------------------ | -------------------------------- | ------ |
| Add Student    | Valid student details          | Student record is added          | Pass   |
| Add Student    | Invalid age                    | Error message is displayed       | Pass   |
| Add Student    | Invalid phone number           | Error message is displayed       | Pass   |
| View Students  | Select View Students           | Student records are displayed    | Pass   |
| Search Student | Valid Student ID               | Matching student is displayed    | Pass   |
| Add Room       | Valid room details             | Room is added                    | Pass   |
| Add Fee        | Valid Student ID and amount    | Fee record is added              | Pass   |
| Add Fee        | Invalid Student ID             | Error message is displayed       | Pass   |
| Add Complaint  | Valid Student ID and complaint | Complaint is submitted           | Pass   |
| Add Complaint  | Empty complaint                | Error message is displayed       | Pass   |
| Attendance     | Entry/Exit selected            | Attendance is recorded           | Pass   |
| Search Records | ID with no matching record     | Appropriate message is displayed | Pass   |
| Reports        | Select re                      |                                  |        |
