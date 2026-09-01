import unittest
from unittest.mock import patch
from main import Student, StudentManagementSystem, get_valid_age, get_valid_marks, get_valid_id, get_valid_text, \
    validate_student_data, validate_dict


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

    def test_load_students_empty_file(self):
        system = StudentManagementSystem()
        with patch("builtins.open") as mock_open:
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.read.return_value = ""
            result = system.load_students()
        self.assertTrue(result)
        self.assertEqual(system.students, [])

    def test_load_students_invalid_json_file(self):
        system = StudentManagementSystem()
        with patch("builtins.open") as mock_open:
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.read.return_value = "Hello"
            with patch("builtins.print") as mock_print:
                result = system.load_students()
        self.assertFalse(result)
        mock_print.assert_any_call("There seems to be an error with students data\nKindly handle it.")

    def test_load_students_reject_invalid_data(self):
        system = StudentManagementSystem()
        with patch("builtins.open") as mock_open:
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.read.return_value = '{"student": 1}'
            with patch("builtins.print") as mock_print:
                result = system.load_students()
        mock_print.assert_any_call("Loading data failed because the JSON data must be a list.")
        self.assertFalse(result)

    def test_save_students_check_os_error(self):
        system = StudentManagementSystem()
        with patch("builtins.open") as mock_open:
            mock_open.side_effect = OSError
            result = system.save_students()
        self.assertFalse(result)

    def test_save_students_expected_data(self):
        student = Student(1, "Namel", 22, "Computer Engineering", 90)
        system = StudentManagementSystem([student])
        with patch("builtins.open") as mock_open:
            with patch("json.dump") as mock_dump:
                result = system.save_students()

        mock_dump.assert_called_once_with(
            [{
                "student_id": 1,
                "name": "Namel",
                "age": 22,
                "department": "Computer Engineering",
                "marks": 90
            }],
            mock_open.return_value.__enter__.return_value,
            indent=4
        )
        self.assertTrue(result)

    def test_invalid_student_not_appended(self):
        system = StudentManagementSystem()
        system.convert_students(["hello"])
        self.assertEqual(system.students, [])

    def test_duplicate_id_student_not_appended(self):
        system = StudentManagementSystem()
        data = [
            {
                "student_id": 1,
                "name": "Minahil",
                "age": 21,
                "department": "Computer Engineering",
                "marks": 90
            },
            {
                "student_id": 1,
                "name": "Ayesha",
                "age": 22,
                "department": "Electrical Engineering",
                "marks": 85
            }
        ]
        system.convert_students(data)
        self.assertEqual(len(system.students), 1)

    def test_valid_student_appended(self):
        system = StudentManagementSystem()
        data = [
            {
                "student_id": 1,
                "name": "Minahil",
                "age": 21,
                "department": "Computer Engineering",
                "marks": 90
            },
            {
                "student_id": 2,
                "name": "Ayesha",
                "age": 22,
                "department": "Electrical Engineering",
                "marks": 85
            }
        ]
        system.convert_students(data)
        self.assertEqual(len(system.students), 2)

    def test_wrong_data_type_id(self):
        data = {
            "student_id": "abc",
            "name": "Minahil",
            "age": 21,
            "department": "Computer Engineering",
            "marks": 90
        }

        with patch("builtins.print") as mock_print:
            result = validate_student_data(data)

        self.assertFalse(result)
        mock_print.assert_any_call("Student ID is not an integer.")

    def test_negative_id_student(self):
        data = {
            "student_id": -1,
            "name": "Minahil",
            "age": 21,
            "department": "Computer Engineering",
            "marks": 90
        }
        with patch("builtins.print") as mock_print:
            result = validate_student_data(data)

        self.assertFalse(result)
        mock_print.assert_any_call("Student ID is negative.")

    def test_wrong_data_type_name(self):
        data = {
            "student_id": 1,
            "name": 123,
            "age": 21,
            "department": "Computer Engineering",
            "marks": 90
        }
        with patch("builtins.print") as mock_print:
            result = validate_student_data(data)

        self.assertFalse(result)
        mock_print.assert_any_call("Student name is not a string.")

    def test_empty_name(self):
        data = {
            "student_id": 1,
            "name": "",
            "age": 21,
            "department": "Computer Engineering",
            "marks": 90
        }

        with patch("builtins.print") as mock_print:
            result = validate_student_data(data)

        self.assertFalse(result)
        mock_print.assert_any_call("Student name can't be empty.")

    def test_invalid_name(self):
        data = {
            "student_id": 1,
            "name": "M123",
            "age": 21,
            "department": "Computer Engineering",
            "marks": 90
        }
        with patch("builtins.print") as mock_print:
            result = validate_student_data(data)

        self.assertFalse(result)
        mock_print.assert_any_call(
            "Student name doesn't contain only letters and spaces."
        )

    def test_wrong_data_type_age(self):
        data = {
            "student_id": 1,
            "name": "Minahil",
            "age": "21",
            "department": "Computer Engineering",
            "marks": 90
        }

        with patch("builtins.print") as mock_print:
            result = validate_student_data(data)

        self.assertFalse(result)
        mock_print.assert_any_call("Student age is not an integer.")

    def test_age_below_minimum_student(self):
        data = {
            "student_id": 1,
            "name": "Minahil",
            "age": 14,
            "department": "Computer Engineering",
            "marks": 90
        }
        with patch("builtins.print") as mock_print:
            result = validate_student_data(data)

        self.assertFalse(result)
        mock_print.assert_any_call(
            "Student age must be between 15 and 30."
        )

    def test_age_above_maximum_student(self):
        data = {
            "student_id": 1,
            "name": "Minahil",
            "age": 31,
            "department": "Computer Engineering",
            "marks": 90
        }

        with patch("builtins.print") as mock_print:
            result = validate_student_data(data)
        self.assertFalse(result)
        mock_print.assert_any_call(
            "Student age must be between 15 and 30."
        )

    def test_wrong_data_type_department(self):
        data = {
            "student_id": 1,
            "name": "Minahil",
            "age": 21,
            "department": 123,
            "marks": 90
        }

        with patch("builtins.print") as mock_print:
            result = validate_student_data(data)

        self.assertFalse(result)
        mock_print.assert_any_call(
            "Student department is not a string."
        )

    def test_empty_department(self):
        data = {
            "student_id": 1,
            "name": "Minahil",
            "age": 21,
            "department": "",
            "marks": 90
        }

        with patch("builtins.print") as mock_print:
            result = validate_student_data(data)

        self.assertFalse(result)
        mock_print.assert_any_call(
            "Student department can't be empty."
        )

    def test_invalid_department(self):
        data = {
            "student_id": 1,
            "name": "Minahil",
            "age": 21,
            "department": "Computer123",
            "marks": 90
        }

        with patch("builtins.print") as mock_print:
            result = validate_student_data(data)
        self.assertFalse(result)
        mock_print.assert_any_call("Student department must contain only letters and spaces.")

    def test_wrong_data_type_marks(self):
        data = {
            "student_id": 1,
            "name": "Minahil",
            "age": 21,
            "department": "Computer Engineering",
            "marks": "90"
        }
        with patch("builtins.print") as mock_print:
            result = validate_student_data(data)

        self.assertFalse(result)
        mock_print.assert_any_call("Student marks is not an integer")

    def test_marks_below_minimum_student(self):
        data = {
            "student_id": 1,
            "name": "Minahil",
            "age": 21,
            "department": "Computer Engineering",
            "marks": -1
        }

        with patch("builtins.print") as mock_print:
            result = validate_student_data(data)

        self.assertFalse(result)
        mock_print.assert_any_call("Student marks are not between 0-100")

    def test_marks_above_maximum_student(self):
        data = {
            "student_id": 1,
            "name": "Minahil",
            "age": 21,
            "department": "Computer Engineering",
            "marks": 101
        }

        with patch("builtins.print") as mock_print:
            result = validate_student_data(data)

        self.assertFalse(result)
        mock_print.assert_any_call("Student marks are not between 0-100")

    def test_valid_student_data(self):
        data = {
            "student_id": 1,
            "name": "Minahil",
            "age": 21,
            "department": "Computer Engineering",
            "marks": 90
        }
        result = validate_student_data(data)

        self.assertTrue(result)

    def test_validate_dict_non_dictionary(self):
        with patch("builtins.print") as mock_print:
            result = validate_dict("hello")

        self.assertFalse(result)
        mock_print.assert_any_call("Skipping this student.")

    def test_validate_dict_missing_required_field(self):
        data = {
            "student_id": 1,
            "name": "Minahil",
            "age": 21,
            "department": "Computer Engineering"
        }

        with patch("builtins.print") as mock_print:
            result = validate_dict(data)

        self.assertFalse(result)
        mock_print.assert_any_call("Student data is missing a required field.")
        mock_print.assert_any_call("Skipping this student.")

    def test_validate_dict_invalid_student_data(self):
        data = {
            "student_id": 1,
            "name": "Minahil123",
            "age": 21,
            "department": "Computer Engineering",
            "marks": 90
        }

        with patch("builtins.print") as mock_print:
            result = validate_dict(data)

        self.assertFalse(result)
        mock_print.assert_any_call("Skipping this student.")

    def test_validate_dict_valid_student_data(self):
        data = {
            "student_id": 1,
            "name": "Minahil",
            "age": 21,
            "department": "Computer Engineering",
            "marks": 90
        }

        result = validate_dict(data)

        self.assertTrue(result)

    def test_add_student(self):
        system = StudentManagementSystem()
        with patch("builtins.input",side_effect = ["1","Minahil","21","Computer Engineering","90"]):
            with patch.object(system,"save_students",return_value = True):
                system.add_student()
        self.assertEqual(len(system.students), 1)
        self.assertEqual(system.students[0].id, 1)
        self.assertEqual(system.students[0].name, "Minahil")

    def test_add_student_duplicate_id(self):
        existing_student = Student(1, "Ayesha", 21, "Computer Engineering", 85)
        system = StudentManagementSystem([existing_student])
        with patch("builtins.input", side_effect=["1","2","Minahil","21","Computer Engineering","90"]):
            with patch.object(system, "save_students", return_value=True):
                system.add_student()
        self.assertEqual(len(system.students), 2)
        self.assertEqual(system.students[1].id, 2)
        self.assertEqual(system.students[1].name, "Minahil")

    def test_add_student_save_failure(self):
        system = StudentManagementSystem()
        with patch("builtins.input", side_effect=["1","Minahil","21","Computer Engineering","90"]):
            with patch.object(system, "save_students", return_value=False):
                system.add_student()
        self.assertEqual(system.students, [])