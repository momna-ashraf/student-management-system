import sqlite3


class Database:

    def __init__(self, database_name="students.db"):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL CHECK (age BETWEEN 15 AND 30),
                department TEXT NOT NULL,
                marks INTEGER NOT NULL CHECK (marks BETWEEN 0 AND 100)
            )
        """)
        self.connection.commit()

    def add_student(self, student_id, name, age, department, marks):
        try:
            self.cursor.execute("""
            Insert into students (id,name,age,department,marks)
            Values(?,?,?,?,?)""", (student_id, name, age, department, marks))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_all_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def get_student_by_id(self, student_id):
        self.cursor.execute("SELECT * FROM students WHERE id =?", (student_id,))
        return self.cursor.fetchone()

    def update_student(self, student_id, field, new_value):
        allowed_fields = {"name", "age", "department", "marks"}

        if field not in allowed_fields:
            return False

        try:
            self.cursor.execute(f"UPDATE students SET {field}= ? WHERE id = ?", (new_value, student_id))
            self.connection.commit()
            return self.cursor.rowcount > 0

        except sqlite3.IntegrityError:
            return False

    def delete_student(self, student_id):
        self.cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )
        self.connection.commit()
        return self.cursor.rowcount > 0

    def close(self):
        self.connection.close()
