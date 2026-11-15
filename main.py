from student_management_system import StudentManagementSystem
from user_interface import UI
def main():
    system = StudentManagementSystem()
    ui = UI(system)
    try:
        ui.run()

    finally:
            system.db.close()


if __name__ == "__main__":
    main()
