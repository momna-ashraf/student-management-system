import unittest
from unittest.mock import patch, Mock
from student import Student
from user_interface import UI


class TestUserInterface(unittest.TestCase):
    def setUp(self):
        self.system = Mock()
        self.ui = UI(self.system)

    def test_validate_age(self):
        with patch("builtins.input", return_value="23"):
            result = self.ui.get_valid_age("Enter age: ")
        self.assertEqual(result, 23)

    def test_age_below_minimum(self):
        with patch("builtins.input", side_effect=["14", "20"]):
            result = self.ui.get_valid_age("Enter age: ")
        self.assertEqual(result, 20)

    def test_age_above_maximum(self):
        with patch("builtins.input", side_effect=["100", "29"]):
            result = self.ui.get_valid_age("Enter age: ")
        self.assertEqual(result, 29)

    def test_age_non_numeric_input(self):
        with patch("builtins.input", side_effect=["Hello", "22"]):
            result = self.ui.get_valid_age("Enter age: ")
        self.assertEqual(result, 22)

    def test_age_empty_input(self):
        with patch("builtins.input", side_effect=["", "23"]):
            result = self.ui.get_valid_age("Enter age: ")
        self.assertEqual(result, 23)

    def test_validate_marks(self):
        with patch("builtins.input", return_value="90"):
            result = self.ui.get_valid_marks("Enter marks: ")
        self.assertEqual(result, 90)

    def test_marks_below_minimum(self):
        with patch("builtins.input", side_effect=["-1", "44"]):
            result = self.ui.get_valid_marks("Enter marks: ")
        self.assertEqual(result, 44)

    def test_marks_above_maximum(self):
        with patch("builtins.input", side_effect=["110", "100"]):
            result = self.ui.get_valid_marks("Enter marks: ")
        self.assertEqual(result, 100)

    def test_marks_non_numeric_input(self):
        with patch("builtins.input", side_effect=["Hello", "22"]):
            result = self.ui.get_valid_marks("Enter marks: ")
        self.assertEqual(result, 22)

    def test_marks_empty_input(self):
        with patch("builtins.input", side_effect=["", "44"]):
            result = self.ui.get_valid_marks("Enter marks: ")
        self.assertEqual(result, 44)

    def test_validate_id(self):
        with patch("builtins.input", return_value="1"):
            result = self.ui.get_valid_id("Enter id: ")
        self.assertEqual(result, 1)

    def test_negative_id(self):
        with patch("builtins.input", side_effect=["-1", "2"]):
            result = self.ui.get_valid_id("Enter id: ")
        self.assertEqual(result, 2)

    def test_non_numeric_id(self):
        with patch("builtins.input", side_effect=["hi", "2"]):
            result = self.ui.get_valid_id("Enter id: ")
        self.assertEqual(result, 2)

    def test_id_empty_input(self):
        with patch("builtins.input", side_effect=["", "23"]):
            result = self.ui.get_valid_id("Enter id: ")
        self.assertEqual(result, 23)

    def test_valid_text_input(self):
        with patch("builtins.input", return_value="Computer"):
            result = self.ui.get_valid_text("Enter text: ", "Department")
        self.assertEqual(result, "Computer")

    def test_text_empty_input(self):
        with patch("builtins.input", side_effect=["", "Computer"]):
            result = self.ui.get_valid_text("Enter text: ", "Department")
        self.assertEqual(result, "Computer")

    def test_text_non_alphabetic_input(self):
        with patch("builtins.input", side_effect=["#", "12", "Computer"]):
            result = self.ui.get_valid_text("Enter text: ", "Department")
        self.assertEqual(result, "Computer")

    def test_display_students(self):
        student = Student(1, "Minahil", 20, "Computer Engineering", 90)

        with patch("builtins.print") as mock_print:
            self.ui.display_student(student)

        mock_print.assert_any_call("Student Name: Minahil")
        mock_print.assert_any_call("ID: 1")
        mock_print.assert_any_call("Age: 20")
        mock_print.assert_any_call("Department: Computer Engineering")
        mock_print.assert_any_call("Marks: 90")


if __name__ == "__main__":
    unittest.main()
