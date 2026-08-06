def display_menu():
    print("\n========== Student Management System ============")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


students = [
    {
        "id": 101,
        "name": "Ali",
        "age": 20,
        "department": "CE",
        "marks": 85
    },
    {
        "id": 102,
        "name": "Alisha",
        "age": 19,
        "department": "CS",
        "marks": 90
    }
]


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


def find_student_by_id(student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return None


def display_student(student):
    print("--------------------------")
    for key, value in student.items():
        print(f"{key.capitalize()}: {value}")
    print("--------------------------")


def add_student():
    print("\n======= Add Student ========")
    while True:
        student_id = get_valid_id("Enter student ID: ")
        if find_student_by_id(student_id):
            print("ID must be unique.")
            continue
        break

    student_name = get_valid_name("Enter student name: ")

    student_age = get_valid_age("Enter student age: ")

    department_name = get_valid_department("Enter student department: ")

    student_marks = get_valid_marks("Enter student marks: ")

    student = {
        "id": student_id,
        "name": student_name,
        "age": student_age,
        "department": department_name,
        "marks": student_marks
    }
    students.append(student)
    print("Student added successfully!\n")


def view_students():
    print("\n======= View Students ========")
    if not students:
        print("No students found.")
        return

    num = 1
    print("\n====== Students list ========")
    for student in students:
        print(f"\nStudent {num}")
        display_student(student)
        num += 1


def search_student():
    print("\n======= Search Student ========")
    student_id = get_valid_id("Enter the student ID to search:")
    student = find_student_by_id(student_id)

    if student:
        print("Student found successfully")
        display_student(student)
    else:
        print("Student not found.")


def update_student():
    print("\n======= Update Student ========")
    update_student_id = get_valid_id("Enter ID of student you want to update: ")
    student = find_student_by_id(update_student_id)
    if not student:
        print("Student not found.")
        return

    display_student(student)

    while True:
        x = input(
            "What you wanna update (name, age, department, marks): "
        ).lower().strip()

        if x == "name":
            student["name"] = get_valid_name("Enter Student's new name: ")
            print("Updated successfully!")
            break

        elif x == "age":
            student["age"] = get_valid_age("Enter student's new age: ")
            print("Updated successfully!")
            break

        elif x == "department":
            student["department"] = get_valid_department("Enter student's new department: ")
            print("Updated successfully!")
            break

        elif x == "marks":
            student["marks"] = get_valid_marks("Enter student's new marks: ")
            print("Updated successfully!")
            break
        else:
            print("Please enter a valid choice.")


def delete_student():
    print("\n======= Delete Student ========")
    id_delete = get_valid_id("Enter student ID to delete: ")

    student = find_student_by_id(id_delete)

    if student:
        display_student(student)
        students.remove(student)
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def main():
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_student()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            print("Thank you for using Student Management System")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
