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