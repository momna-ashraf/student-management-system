# Student Management System

A console-based **Student Management System built with Python**, developed incrementally to practice programming, software design, Object-Oriented Programming, database management, application architecture, testing, and Git/GitHub.

## Features

- Add, view, search, update, and delete students
- Input validation for student data
- Object-Oriented Programming with `Student` and `StudentManagementSystem`
- SQLite database integration using Python's `sqlite3` module
- Layered application architecture with separate responsibilities
- Dedicated database layer using a `Database` class
- Parameterized SQL queries
- Database-level constraints and duplicate ID prevention
- Proper database connection management
- Unit testing with Python's `unittest` framework

## Student Information

Each student record contains:

- Student ID
- Name
- Age
- Department
- Marks

## Validation Rules

- Student ID must be a non-negative, unique integer
- Name and department cannot be empty
- Name and department may contain only letters and spaces
- Age must be between 15 and 30
- Marks must be between 0 and 100

## Application Architecture

The project follows a layered structure to separate user interaction, application logic, data management, and student representation.

### Project Structure

```text
Student Management System/
│
├── main.py
├── student.py
├── database.py
├── student_management_system.py
├── user_interface.py
│
├── test_database.py
├── test_user_interface.py
│
├── .gitignore
├── README.md
└── students.db
```

### Module Responsibilities

| Module | Responsibility |
|---|---|
| `main.py` | Application entry point and object initialization |
| `student.py` | Student data model |
| `database.py` | SQLite database operations and persistence |
| `student_management_system.py` | Application logic and coordination |
| `user_interface.py` | Menu, user input, validation, and output |

### Application Flow

```text
User Interface
      ↓
Student Management System
      ↓
Database
```

The `Student` model represents student records and is used by the application and user interface layers.

## Database Structure

The application uses SQLite for persistent data storage.

**Database table: `students`**

| Column | Data Type | Constraint |
|---|---|---|
| id | INTEGER | PRIMARY KEY |
| name | TEXT | NOT NULL |
| age | INTEGER | NOT NULL, CHECK (15–30) |
| department | TEXT | NOT NULL |
| marks | INTEGER | NOT NULL, CHECK (0–100) |

The database is automatically created when the application runs if it does not already exist.

## Testing

The project uses Python's built-in `unittest` framework.

**Test files:**

- `test_database.py` — Tests SQLite database operations, including adding, retrieving, updating, and deleting students, duplicate IDs, and database constraints.
- `test_user_interface.py` — Tests user input validation and interface-related behavior.

Run the complete test suite:

```bash
python -m unittest discover
```

## Technologies

- Python 3
- SQLite
- `sqlite3`
- `unittest`
- Git & GitHub
- PyCharm

## Project Roadmap

| Version | Focus | Status |
|---|---|---|
| 1 | Basic CRUD | ✅ |
| 2 | Refactoring & validation | ✅ |
| 3 | JSON persistence | ✅ |
| 4 | Object-Oriented Programming | ✅ |
| 5 | OOP + JSON integration | ✅ |
| 6 | Robust JSON validation | ✅ |
| 7 | Refactoring & maintainability | ✅ |
| 8 | Testing & project organization | ✅ |
| 9 | SQLite database integration | ✅ |
| 10 | Application architecture | ✅ |
| 11 | Final refactoring & code quality | ⏳ |
| 12 | Tkinter GUI | ⏳ |
| 1.0 | Final documentation, screenshots & release | ⏳ |

## Getting Started

### Prerequisites

- Python 3 installed on your system
- Git installed on your system

### Installation

1. Clone the repository:

```bash
git clone https://github.com/momna-ashraf/student-management-system.git
```

2. Navigate to the project directory:

```bash
cd student-management-system
```

3. Run the application:

```bash
python main.py
```

The SQLite database file will be created automatically when the application starts.

## Future Development

- Final code refactoring and quality improvements
- Tkinter graphical user interface
- Final documentation, screenshots, and project release

---

**Built as a learning project to develop practical Python and software engineering skills.**