from student import Student


class UI:
    def __init__(self, system):
        self.system = system

    def run(self):
        menu_actions = {
            1: self.add_student,
            2: self.view_students,
            3: self.search_student,
            4: self.update_student,
            5: self.delete_student,
        }

        while True:
            self.display_menu()

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

    def display_menu(self):
        print("\n========== Student Management System ============")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

    def add_student(self):
        print("\n======= Add Student ========")

        student_id = self.get_valid_id("Enter student ID: ")
        if self.system.find_student_by_id(student_id):
            print("Student ID already exists. Please try another ID.")
            return
        student_name = self.get_valid_text("Enter student name: ", "Name")
        student_age = self.get_valid_age("Enter student age: ")
        department_name = self.get_valid_text(
            "Enter student department: ", "Department"
        )
        student_marks = self.get_valid_marks("Enter student marks: ")

        student = Student(
            student_id,
            student_name,
            student_age,
            department_name,
            student_marks
        )

        added = self.system.add_student(student)

        if added:
            print("Student added successfully!\n")
        else:
            print("Could not add student. ID may already exist or database operation failed.")

    def search_student(self):
        print("\n======= Search Student ========")
        student_id = self.get_valid_id("Enter the student ID to search:")
        student = self.system.search_student(student_id)
        if student:
            print("Student found successfully")
            student.display_student()
        else:
            print("Student not found.")

    def view_students(self):
        students = self.system.view_students()
        print("\n======= View Students ========")
        if not students:
            print("No students found.")
            return
        else:
            print("\n====== Students list ========")
            for student in students:
                student.display_student()

    def update_student(self):
        print("\n======= Update Student ========")

        student_id = self.get_valid_id(
            "Enter ID of student you want to update: "
        )

        student = self.system.find_student_by_id(student_id)

        if not student:
            print("Student not found.")
            return

        student.display_student()

        validators = {
            "name": lambda message: self.get_valid_text(message, "Name"),
            "age": self.get_valid_age,
            "department": lambda message: self.get_valid_text(message, "Department"),
            "marks": self.get_valid_marks
        }

        while True:
            to_update = input(
                "What do you want to update (name, age, department, marks): "
            ).lower().strip()

            if to_update not in validators:
                print("Please enter a valid choice.")
                continue

            new_value = validators[to_update](
                f"Enter student's new {to_update}: "
            )

            updated = self.system.update_student(
                student_id, to_update, new_value
            )

            if updated:
                print("Updated successfully!\n")
            else:
                print("Could not update student data.")

            break

    def delete_student(self):
        print("\n======= Delete Student ========")
        id_delete = self.get_valid_id("Enter student ID to delete: ")

        student = self.system.find_student_by_id(id_delete)

        if student:
            student.display_student()
            deleted = self.system.delete_student(id_delete)
            if not deleted:
                print("Could not delete student data.")
            else:
                print("Student deleted successfully!")
        else:
            print("Student not found.")

    def get_valid_age(self, message):
        while True:
            try:
                age = int(input(message))
                if age < 15 or age > 30:
                    print("Age must be between 15 and 30")
                    continue
                return age
            except ValueError:
                print("Age must be a number")

    def get_valid_text(self, message, field_name):
        while True:
            value = input(message).strip()
            if value == "":
                print(f"{field_name} can't be empty")
                continue

            if value.replace(" ", "").isalpha():
                return value.title()

            print(f"{field_name} should contain only letters and spaces.")

    def get_valid_marks(self, message):
        while True:
            try:
                marks = int(input(message))
                if 0 <= marks <= 100:
                    return marks
                print("Marks must be between 0 to 100")
            except ValueError:
                print("Please enter a valid integer for the marks.")

    def get_valid_id(self, message):
        while True:
            try:
                student_id = int(input(message))
                if student_id < 0:
                    print("Student ID cannot be negative.")
                    continue

                return student_id
            except ValueError:
                print("Please enter a valid integer for the Student ID.")
