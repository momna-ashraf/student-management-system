# Student Management System

A console-based Student Management System built in Python to practice software development principles and showcase programming skills.

## Project Description

This project is being developed incrementally to strengthen my understanding of Python programming, problem solving, software design, Object-Oriented Programming, file handling, error handling, Git, and GitHub.

Each version introduces new concepts while improving the project's structure and maintainability.

---

## Current Features (Version 5)

* Add a new student
* View all students
* Search for a student by ID
* Update student information
* Delete student
* Input validation for all fields
* Reusable helper functions
* Object-Oriented Programming (OOP)
* JSON-based data persistence
* Automatically load student records when the program starts
* Handle missing required fields in stored JSON data

---

## Student Information

Each student record contains:

* Student ID
* Name
* Age
* Department
* Marks

---

## Rules

* Every Student ID must be unique.
* Student ID cannot be negative.
* Name cannot be empty and must contain only letters and spaces.
* Age must be between 15 and 30.
* Department cannot be empty and must contain only letters and spaces.
* Marks must be between 0 and 100.

---

## Technologies Used

* Python 3
* PyCharm IDE
* Git
* GitHub
* JSON

---

## Project Roadmap

### ✅ Version 1

* Basic CRUD operations

### ✅ Version 2

* Code refactoring
* Reusable helper functions
* Input validation
* Cleaner and more maintainable code

### ✅ Version 3

* Save student records to a JSON file
* Load student records automatically

### ✅ Version 4

* Convert the system to Object-Oriented Programming (OOP)
* Introduce `Student` and `StudentManagementSystem` classes

### ✅ Version 5 (Current)

* Integrate JSON persistence with the OOP structure
* Convert Student objects to dictionaries for JSON storage
* Reconstruct Student objects when loading data
* Handle missing required fields in JSON data

### 🔄 Version 6 (Next)

* Refactor and improve code structure
* Improve error handling
* Reduce repetition
* Improve overall maintainability

---

## Future Improvements

* SQLite database
* Graphical User Interface (GUI)
* Web version using Flask
* User authentication and authorization
