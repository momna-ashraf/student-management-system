import unittest
from unittest.mock import patch
from main import Student, StudentManagementSystem, get_valid_age, get_valid_marks, get_valid_id, get_valid_text


class TestStudentManagementSystem(unittest.TestCase):
    def test_find_existing_student(self):
        student = Student(1, "Minahil Ashgar", 23, "Electrical Engineering", 88)
        system = StudentManagementSystem([student])

        result = system.find_student_by_id(1)
        self.assertEqual(result, student)

    def test_find_missing_student(self):
        student = Student(1, "Minahil Ashgar", 23, "Electrical Engineering", 88)
        system = StudentManagementSystem([student])

        result = system.find_student_by_id(2)
        self.assertIsNone(result)

    def test_validate_age(self):
        with patch("builtins.input", return_value=23):
            result = get_valid_age("Enter age: ")
        self.assertEqual(result, 23)

    def test_age_below_minimum(self):
        with patch("builtins.input", side_effect=["14", "20"]):
            result = get_valid_age("Enter age: ")
        self.assertEqual(result, 20)

    def test_age_above_maximum(self):
        with patch("builtins.input", side_effect=["100", "29"]):
            result = get_valid_age("Enter age: ")
        self.assertEqual(result, 29)

    def test_age_non_numeric_input(self):
        with patch("builtins.input", side_effect=["Hello", "22"]):
            result = get_valid_age("Enter age: ")
        self.assertEqual(result, 22)

    def test_age_empty_input(self):
        with patch("builtins.input", side_effect=["", "23"]):
            result = get_valid_age("Enter age: ")
        self.assertEqual(result, 23)

    def test_validate_marks(self):
        with patch("builtins.input", return_value="90"):
            result = get_valid_marks("Enter marks: ")
        self.assertEqual(result, 90)

    def test_marks_below_minimum(self):
        with patch("builtins.input", side_effect=["-1", "44"]):
            result = get_valid_marks("Enter marks: ")
        self.assertEqual(result, 44)

    def test_marks_above_maximum(self):
        with patch("builtins.input", side_effect=["110", "100"]):
            result = get_valid_marks("Enter marks: ")
        self.assertEqual(result, 100)

    def test_marks_non_numeric_input(self):
        with patch("builtins.input", side_effect=["Hello", "22"]):
            result = get_valid_marks("Enter marks: ")
        self.assertEqual(result, 22)

    def test_marks_empty_input(self):
        with patch("builtins.input", side_effect=["", "44"]):
            result = get_valid_marks("Enter marks: ")
        self.assertEqual(result, 44)

    def test_validate_id(self):
        with patch("builtins.input", return_value="1"):
            result = get_valid_id("Enter id: ")
        self.assertEqual(result, 1)

    def test_negative_id(self):
        with patch("builtins.input", side_effect=["-1", "2"]):
            result = get_valid_id("Enter id: ")
        self.assertEqual(result, 2)

    def test_non_numeric_id(self):
        with patch("builtins.input", side_effect=["hi", "2"]):
            result = get_valid_id("Enter id: ")
        self.assertEqual(result, 2)

    def test_id_empty_input(self):
        with patch("builtins.input", side_effect=["", "23"]):
            result = get_valid_id("Enter id: ")
        self.assertEqual(result, 23)

    def test_valid_text_input(self):
        with patch("builtins.input", return_value="Computer"):
            result = get_valid_text("Enter text: ", "Department")
        self.assertEqual(result, "Computer")

    def test_text_empty_input(self):
        with patch("builtins.input", side_effect=["", "Computer"]):
            result = get_valid_text("Enter text: ", "Department")
        self.assertEqual(result, "Computer")

    def test_text_non_alphabetic_input(self):
        with patch("builtins.input", side_effect=["#", "12", "Computer"]):
            result = get_valid_text("Enter text: ", "Department")
        self.assertEqual(result, "Computer")

    def test_student_to_dict(self):
        student = Student(1, "Minahil", 21, "Computer Science", 90)

        result = student.to_dict()

        self.assertEqual(result, {
            "student_id": 1,
            "name": "Minahil",
            "age": 21,
            "department": "Computer Science",
            "marks": 90
        })

    def test_display_students(self):
        student = Student(1, "Minahil", 20, "Computer Engineering", 90)
        with patch("builtins.print") as mock_print:
            student.display_student()
        mock_print.assert_any_call("Student Name: Minahil")
        mock_print.assert_any_call("ID: 1")
        mock_print.assert_any_call("Age: 20")
        mock_print.assert_any_call("Department: Computer Engineering")
        mock_print.assert_any_call("Marks: 90")

    def test_system_initialization(self):
        system = StudentManagementSystem()
        result = system.students
        self.assertEqual(result, [])

    def test_system_initialization_students(self):
        student = Student(1, "Minahil", 21, "Computer Science", 90)
        system = StudentManagementSystem([student])
        result = system.students
        self.assertEqual(result, [student])

    def test_load_students_file_not_found(self):
        system = StudentManagementSystem()
        with patch("builtins.open") as mock_open:
            mock_open.side_effect = FileNotFoundError
            result = system.load_students()
        self.assertTrue(result)
        self.assertEqual(system.students, [])
