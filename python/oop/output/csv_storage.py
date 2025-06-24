import csv
import os

from python.oop.entities import User
from python.oop.interfaces import UserStorageAdapterInterface


class CSVStorageAdapter(UserStorageAdapterInterface):
    """Store tutors and students in separate CSV files."""

    def __init__(self, directory: str):
        self.tutor_file_path = os.path.join(directory, "tutors.csv")
        self.student_file_path = os.path.join(directory, "students.csv")
        self._ensure_csv_has_headers()

    def _ensure_csv_has_headers(self):
        """Ensure the CSV files exist and have headers."""
        for path in (self.tutor_file_path, self.student_file_path):
            if not os.path.isfile(path):
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        [
                            "id",
                            "name",
                            "surname",
                            "role",
                            "password",
                            "email",
                            "subject",
                            "grade",
                        ]
                    )

    def save_user(self, user: User) -> None:
        """Save a single user to the appropriate CSV."""
        path = self.tutor_file_path if user.role == "tutor" else self.student_file_path
        with open(path, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(self._user_to_row(user))

    def save_users_bulk(self, users: list[User]) -> None:
        """Save multiple users to their respective CSV files."""
        tutors = [u for u in users if u.role == "tutor"]
        students = [u for u in users if u.role == "student"]

        if tutors:
            with open(self.tutor_file_path, mode="a", newline="") as file:
                writer = csv.writer(file)
                for user in tutors:
                    writer.writerow(self._user_to_row(user))

        if students:
            with open(self.student_file_path, mode="a", newline="") as file:
                writer = csv.writer(file)
                for user in students:
                    writer.writerow(self._user_to_row(user))

    def _user_to_row(self, user: User) -> list:
        """Convert a User object to a CSV row format."""
        if user.role == 'tutor':
            subject = getattr(user, 'subject', '')
            grade = ''
        elif user.role == 'student':
            subject = ''
            grade = getattr(user, 'grade', '')
        else:
            subject = ''
            grade = ''
        return [user.id, user.name, user.surname, user.role, user.password, user.email, subject, grade]
