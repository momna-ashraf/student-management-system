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
    }
]


def add_student():
    print("\n======= Add Student ========")
    while True:
        try:
            student_id = int(input("Enter the student ID: "))
            if student_id < 0:
                print("Student ID cannot be negative.")
                continue
            duplicate_found = False
            for student in students:
                if student["id"] == student_id:
                    duplicate_found = True
                    break
            if duplicate_found:
                print("ID must be unique.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the Student ID.")


    while True:
        student_name = input("Enter the student name: ").strip()
        if student_name == "":
            print("Name can't be empty")
            continue
        if student_name.replace(" ", "").isalpha():
            student_name = student_name.title()
            break
        else:
            print("Name should contain only letters and spaces.")
            continue

    while True:
        try:
            student_age = int(input("Enter the student age: "))
            if student_age < 0:
                print("Age can't be negative")
                continue
            elif student_age < 15 or student_age > 30:
                print("Age must be between 15 and 30")
                continue

            break
        except ValueError:
            print("Age must be a number")

    while True:
        department_name = input("Enter the department name: ").strip()
        if department_name == "":
            print("Department name can't be empty")
            continue
        if department_name.replace(" ", "").isalpha():
            department_name = department_name.title()
            break
        else:
            print("Department name should contain only letters and spaces.")
            continue

    while True:
        try:
            student_marks = int(input("Enter the student marks: "))
            if 0 <= student_marks <= 100:
                break
            else:
                print("Marks must be between 0 to 100")
        except ValueError:
            print("Please enter a valid integer for the marks.")

    student = {
        "id": student_id,
        "name": student_name,
        "age": student_age,
        "department": department_name,
        "marks": student_marks
    }
    students.append(student)
    print("Student added successfully!")


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
            print("Feature coming soon...")

        elif choice == 3:
            print("Feature coming soon...")

        elif choice == 4:
            print("Feature coming soon...")

        elif choice == 5:
            print("Feature coming soon...")

        elif choice == 6:
            print("Thank you for using Student Management System")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
