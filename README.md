# Student Management System

A console-based **Student Management System built with Python**, developed incrementally to practice programming, software design, Object-Oriented Programming, data persistence, testing, and Git/GitHub.

## Features

* Add, view, search, update, and delete students
* Input validation for student data
* Object-Oriented Programming with `Student` and `StudentManagementSystem`
* JSON-based data persistence
* Robust handling of invalid and malformed JSON data
* Duplicate ID detection
* Save-operation rollback on failure
* Unit testing with Python's `unittest` framework
* Comprehensive testing of validation, persistence, and CRUD operations

## Student Information

Each student record contains:

* Student ID
* Name
* Age
* Department
* Marks

## Validation Rules

* Student ID must be a non-negative, unique integer
* Name and department cannot be empty
* Name and department may contain only letters and spaces
* Age must be between 15 and 30
* Marks must be between 0 and 100

## Technologies

* Python 3
* `unittest`
* JSON
* Git & GitHub
* PyCharm

## Project Roadmap

| Version | Focus                          | Status |
| ------- | ------------------------------ | ------ |
| 1       | Basic CRUD                     | ✅      |
| 2       | Refactoring & validation       | ✅      |
| 3       | JSON persistence               | ✅      |
| 4       | Object-Oriented Programming    | ✅      |
| 5       | OOP + JSON integration         | ✅      |
| 6       | Robust JSON validation         | ✅      |
| 7       | Refactoring & maintainability  | ✅      |
| 8       | Testing & project organization | ✅      |
| 9       | SQLite database integration    | 🔄     |
| 10      | Application expansion          | ⏳      |

## Future Plans

* SQLite database
* Flask web application
* GUI
* User authentication and authorization

---

**Built as a learning project to develop practical Python and software engineering skills.**
