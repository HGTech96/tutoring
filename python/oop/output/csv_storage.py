import csv
import os

from oop.university.entities import User
from oop.university.interfaces import UserStorageAdapterInterface


class CSVStorageAdapter(UserStorageAdapterInterface):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._ensure_csv_has_headers()

    def _ensure_csv_has_headers(self):
        """Ensure the CSV file exists and has headers."""
        if not os.path.isfile(self.file_path):
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'name', 'surname', 'role', 'password', 'email', 'subject', 'grade'])

    def save_user(self, user: User) -> None:
        """Save a single user to CSV."""
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self._user_to_row(user))

    def save_users_bulk(self, users: list[User]) -> None:
        """Save multiple users to CSV at once."""
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            for user in users:
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
