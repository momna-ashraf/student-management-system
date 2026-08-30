import json
def display_menu():
    print("\n========== Student Management System ============")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


class StudentManagementSystem():
    def __init__(self, students=None):
        if students is None:
            students = []
        self.students = students

    def add_student(self):
        print("\n======= Add Student ========")
        while True:
            student_id = get_valid_id("Enter student ID: ")
            if self.find_student_by_id(student_id):
                print("ID must be unique.")
                continue
            break

        student_name = get_valid_name("Enter student name: ")

        student_age = get_valid_age("Enter student age: ")

        department_name = get_valid_department("Enter student department: ")

        student_marks = get_valid_marks("Enter student marks: ")

        student = Student(student_id, student_name, student_age, department_name, student_marks)
        self.students.append(student)
        self.save_students()
        print("Student added successfully!\n")

    def view_students(self):
        print("\n======= View Students ========")
        if not self.students:
            print("No students found.")
            return

        num = 1
        print("\n====== Students list ========")
        for student in self.students:
            print(f"\nStudent {num}")
            Student.display_student(student)
            num += 1

    def search_student(self):
        print("\n======= Search Student ========")
        student_id = get_valid_id("Enter the student ID to search:")
        student = self.find_student_by_id(student_id)

        if student:
            print("Student found successfully")
            Student.display_student(student)
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

        while True:
            x = input(
                "What you wanna update (name, age, department, marks): "
            ).lower().strip()
            if x == "name":
                student.name = get_valid_name("Enter Student's new name: ")
                self.save_students()
                print("Updated successfully!")
                break

            elif x == "age":
                student.age = get_valid_age("Enter student's new age: ")
                self.save_students()
                print("Updated successfully!")
                break

            elif x == "department":
                student.department = get_valid_department("Enter student's new department: ")
                self.save_students()
                print("Updated successfully!")
                break

            elif x == "marks":
                student.marks = get_valid_marks("Enter student's new marks: ")
                self.save_students()
                print("Updated successfully!")
                break
            else:
                print("Please enter a valid choice.")

    def delete_student(self):
        print("\n======= Delete Student ========")
        id_delete = get_valid_id("Enter student ID to delete: ")

        student = self.find_student_by_id(id_delete)

        if student:
            student.display_student()
            self.students.remove(student)
            self.save_students()
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def save_students(self):
        student_data = []
        for student in self.students:
            student_data.append(student.to_dict())
        with open("students.json", "w") as file:
            json.dump(student_data, file, indent=4)

    def load_students(self):
        try:
            with open("students.json", "r") as file:
                if file.read().strip() == "":
                    self.students = []
                    return False
                file.seek(0)
                data = json.load(file)
                if not isinstance(data,list):
                    print("Loading data failed.")
                    return True
                for student_data in data:
                    s = Student(
                        student_data["id"],
                        student_data["name"],
                        student_data["age"],
                        student_data["department"],
                        student_data["marks"]
                    )
                    self.students.append(s)
                return False
        except FileNotFoundError:
            self.students = []
            return False
        except json.JSONDecodeError:
            print("Their seems to be an error with students data\nKindly handle it.")
            return True

class Student():
    def __init__(self, id, name, age, department, marks):
        self.id = id
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

    def to_dict(self):
        std_dict = {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "marks": self.marks
        }
        return std_dict


def get_valid_name(message):
    while True:
        name = input(message).strip()

        if name == "":
            print("Name can't be empty")
            continue

        if name.replace(" ", "").isalpha():
            return name.title()
        else:
            print("Name should contain only letters and spaces.")


def get_valid_age(message):
    while True:
        try:
            age = int(input(message))
            if age < 0:
                print("Age can't be negative")
                continue
            elif age < 15 or age > 30:
                print("Age must be between 15 and 30")
                continue
            return age
        except ValueError:
            print("Age must be a number")


def get_valid_department(message):
    while True:
        department = input(message).strip()

        if department == "":
            print("Department name can't be empty")
            continue

        if department.replace(" ", "").isalpha():
            return department.title()
        else:
            print("Department name should contain only letters and spaces.")


def get_valid_marks(message):
    while True:
        try:
            marks = int(input(message))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 to 100")
        except ValueError:
            print("Please enter a valid integer for the marks.")


def get_valid_id(message):
    while True:
        try:
            student_id_valid = int(input(message))
            if student_id_valid < 0:
                print("Student ID cannot be negative.")
                continue

            return student_id_valid
        except ValueError:
            print("Please enter a valid integer for the Student ID.")


def main():
    stop = system.load_students()
    if stop:
        return
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            system.add_student()

        elif choice == 2:
            system.view_students()

        elif choice == 3:
            system.search_student()

        elif choice == 4:
            system.update_student()

        elif choice == 5:
            system.delete_student()

        elif choice == 6:
            print("Thank you for using Student Management System")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = StudentManagementSystem()
    main()
