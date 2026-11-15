from student import Student


class StudentManagementSystem:
    def __init__(self, db):
        self.db = db

    def add_student(self, student):
        if self.find_student_by_id(student.id):
            return False

        added = self.db.add_student(
            student.id,
            student.name,
            student.age,
            student.department,
            student.marks
        )

        return added

    def view_students(self):
        students = self.db.get_all_students()
        return [Student(*student) for student in students]

    def search_student(self, student_id):
        student = self.find_student_by_id(student_id)
        return student

    def update_student(self, student_id, field, new_value):
        return self.db.update_student(student_id, field, new_value)

    def delete_student(self, student_id):
        return self.db.delete_student(student_id)

    def find_student_by_id(self, student_id):
        student = self.db.get_student_by_id(student_id)
        if student is None:
            return None
        else:
            return Student(*student)
