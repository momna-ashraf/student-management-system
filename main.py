from database import Database
def display_menu():
    print("\n========== Student Management System ============")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


class StudentManagementSystem:
    def __init__(self):
        self.db = Database()


    def add_student(self):
        print("\n======= Add Student ========")
        while True:
            student_id = get_valid_id("Enter student ID: ")
            if self.find_student_by_id(student_id):
                print("ID must be unique.")
                continue
            break

        student_name = get_valid_text("Enter student name: ", "Name")

        student_age = get_valid_age("Enter student age: ")

        department_name = get_valid_text("Enter student department: ", "Department")

        student_marks = get_valid_marks("Enter student marks: ")
        added = self.db.add_student(student_id, student_name, student_age, department_name, student_marks)

        if not added:
            print("Could not save student data.")
        else:
            print("Student added successfully!\n")

    def view_students(self):
        students = self.db.get_all_students()
        print("\n======= View Students ========")
        if not students:
            print("No students found.")
            return
        else:
            print("\n====== Students list ========")
            for student in students:
               Student(* student).display_student()

    def search_student(self):
        print("\n======= Search Student ========")
        student_id = get_valid_id("Enter the student ID to search:")
        student = self.find_student_by_id(student_id)

        if student:
            print("Student found successfully")
            student.display_student()
        else:
            print("Student not found.")

    def update_student(self):
        print("\n======= Update Student ========")
        update_student_id = get_valid_id("Enter ID of student you want to update: ")
        student = self.find_student_by_id(update_student_id)
        if not student:
            print("Student not found.")
            return

        student.display_student()
        validators = {
            "name": lambda message: get_valid_text(message, "Name"),
            "age": get_valid_age,
            "department": lambda message: get_valid_text(message, "Department"),
            "marks": get_valid_marks
        }
        while True:
            to_update = input(
                "What do you want to update (name, age, department, marks): "
            ).lower().strip()
            if to_update not in validators:
                print("Please enter a valid choice.")
                continue
            new_value = validators[to_update](f"Enter student's new {to_update}: ")
            updated = self.db.update_student(update_student_id,to_update,new_value)
            if not updated:
                print("Could not update student data.")
            else:
                print("Updated successfully!\n")
            break

    def delete_student(self):
        print("\n======= Delete Student ========")
        id_delete = get_valid_id("Enter student ID to delete: ")

        student = self.find_student_by_id(id_delete)

        if student:
            student.display_student()
            deleted = self.db.delete_student(id_delete)
            if not deleted:
                print("Could not delete student data.")
            else:
                print("Student deleted successfully!")
        else:
            print("Student not found.")

    def find_student_by_id(self, id):
        student = self.db.get_student_by_id(id)
        if student is None:
             return None
        else:
            return Student(*student)

class Student:
    def __init__(self, student_id, name, age, department, marks):
        self.id = student_id
        self.name = name
        self.age = age
        self.department = department
        self.marks = marks

    def display_student(self):
        print("--------------------------")
        print(f"Student Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Marks: {self.marks}")
        print("--------------------------")



def get_valid_age(message):
    while True:
        try:
            age = int(input(message))
            if age < 15 or age > 30:
                print("Age must be between 15 and 30")
                continue
            return age
        except ValueError:
            print("Age must be a number")


def get_valid_text(message, field_name):
    while True:
        value = input(message).strip()
        if value == "":
            print(f"{field_name} can't be empty")
            continue

        if value.replace(" ", "").isalpha():
            return value.title()

        print(f"{field_name} should contain only letters and spaces.")


def get_valid_marks(message):
    while True:
        try:
            marks = int(input(message))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 to 100")
        except ValueError:
            print("Please enter a valid integer for the marks.")


def get_valid_id(message):
    while True:
        try:
            student_id = int(input(message))
            if student_id < 0:
                print("Student ID cannot be negative.")
                continue

            return student_id
        except ValueError:
            print("Please enter a valid integer for the Student ID.")



def main():
    try:
        menu_actions = {
        1: system.add_student,
        2: system.view_students,
        3: system.search_student,
        4: system.update_student,
        5: system.delete_student,

        }
        while True:
            display_menu()
            try:
               choice = int(input("\nEnter your choice: "))
            except ValueError:
               print("Please enter a valid number.")
               continue

            if choice in menu_actions:
               menu_actions[choice]()

            elif choice == 6:
               print("Thank you for using Student Management System")
               break

            else:
               print("Invalid choice. Please try again.")

    finally:
            system.db.close()


if __name__ == "__main__":
    system = StudentManagementSystem()
    main()
