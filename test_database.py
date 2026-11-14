
import unittest
import tempfile
import os

from database import Database


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.db_path = self.temp_db.name
        self.temp_db.close()

        self.db = Database(self.db_path)

    def tearDown(self):

        self.db.close()
        os.unlink(self.db_path)

    def test_add_student(self):
        result = self.db.add_student(1,"Alisha",19,"CE",99)
        self.assertTrue(result)
        student = self.db.get_student_by_id(1)

        self.assertEqual(
            student,
            (1, "Alisha", 19, "CE", 99)
        )

    def test_add_student_duplicate_id(self):
        self.db.add_student(
            1, "Ali", 20, "Computer Engineering", 90
        )

        result = self.db.add_student(
            1, "Ahmed", 21, "Electrical Engineering", 85
        )

        self.assertFalse(result)

        students = self.db.get_all_students()

        self.assertEqual(len(students), 1)

    def test_get_all_students(self):
        self.db.add_student(
            1, "Ali", 20, "Computer Engineering", 90
        )

        self.db.add_student(
            2, "Ahmed", 21, "Electrical Engineering", 85
        )

        students = self.db.get_all_students()

        self.assertEqual(len(students), 2)

        self.assertIn(
            (1, "Ali", 20, "Computer Engineering", 90),
            students
        )

        self.assertIn(
            (2, "Ahmed", 21, "Electrical Engineering", 85),
            students
        )

    def test_get_student_by_id(self):
        self.db.add_student(
            1, "Ali", 20, "Computer Engineering", 90
        )

        self.db.add_student(
            2, "Ahmed", 21, "Electrical Engineering", 85
        )

        student = self.db.get_student_by_id(2)

        self.assertEqual(
            student,
            (2, "Ahmed", 21, "Electrical Engineering", 85)
        )

    def test_get_nonexistent_student(self):
        student = self.db.get_student_by_id(999)

        self.assertIsNone(student)

    def test_update_student_name(self):
        self.db.add_student(1, "Ali", 20, "Computer Engineering", 90)

        result = self.db.update_student(1, "name", "Ahmed")

        self.assertTrue(result)
        self.assertEqual(
            self.db.get_student_by_id(1),
            (1, "Ahmed", 20, "Computer Engineering", 90)
        )

    def test_update_student_age(self):
        self.db.add_student(1, "Ali", 20, "Computer Engineering", 90)

        result = self.db.update_student(1, "age", 22)

        self.assertTrue(result)
        self.assertEqual(self.db.get_student_by_id(1)[2], 22)

    def test_update_student_department(self):
        self.db.add_student(1, "Ali", 20, "Computer Engineering", 90)

        result = self.db.update_student(1, "department", "Electrical Engineering")

        self.assertTrue(result)
        self.assertEqual(self.db.get_student_by_id(1)[3], "Electrical Engineering")

    def test_update_student_marks(self):
        self.db.add_student(1, "Ali", 20, "Computer Engineering", 90)

        result = self.db.update_student(1, "marks", 95)

        self.assertTrue(result)
        self.assertEqual(self.db.get_student_by_id(1)[4], 95)

    def test_update_nonexistent_student(self):
        result = self.db.update_student(999, "name", "Ahmed")

        self.assertFalse(result)

    def test_update_invalid_field(self):
        self.db.add_student(1, "Ali", 20, "Computer Engineering", 90)

        result = self.db.update_student(1, "address", "Lahore")

        self.assertFalse(result)

    def test_update_invalid_age(self):
        self.db.add_student(1, "Ali", 20, "Computer Engineering", 90)

        result = self.db.update_student(1, "age", 40)

        self.assertFalse(result)
        self.assertEqual(self.db.get_student_by_id(1)[2], 20)

    def test_update_invalid_marks(self):
        self.db.add_student(1, "Ali", 20, "Computer Engineering", 90)

        result = self.db.update_student(1, "marks", 150)

        self.assertFalse(result)
        self.assertEqual(self.db.get_student_by_id(1)[4], 90)

    def test_delete_student(self):
        self.db.add_student(1, "Ali", 20, "Computer Engineering", 90)

        result = self.db.delete_student(1)

        self.assertTrue(result)
        self.assertIsNone(self.db.get_student_by_id(1))

    def test_delete_nonexistent_student(self):
        result = self.db.delete_student(999)

        self.assertFalse(result)

    def test_get_all_students_empty_database(self):
        students = self.db.get_all_students()

        self.assertEqual(students, [])


if __name__ == '__main__':
    unittest.main()
