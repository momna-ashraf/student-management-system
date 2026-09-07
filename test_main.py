import unittest
from unittest.mock import patch
from main import Student, StudentManagementSystem, get_valid_age


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
        with patch("builtins.input", side_effect=["14", "10", "20"]):
            result = get_valid_age("Enter age: ")
        self.assertEqual(result, 20)

    def test_age_above_maximum(self):
        with patch("builtins.input", side_effect=["100", "44", "29"]):
            result = get_valid_age("Enter age: ")
        self.assertEqual(result, 29)

    def test_age_non_numeric_input(self):
        with patch("builtins.input", side_effect=["Hello", "yes", "22"]):
            result = get_valid_age("Enter age: ")
        self.assertEqual(result, 22)
