from database import Database
from student_management_system import StudentManagementSystem
from user_interface import UI


def main():
    db = Database()
    system = StudentManagementSystem(db)
    ui = UI(system)
    try:
        ui.run()
    finally:
        db.close()


if __name__ == "__main__":
    main()
