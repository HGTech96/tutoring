# user_management/domain/entities.py

from abc import ABC
from typing import Optional
import uuid


class User(ABC):
    def __init__(self, name: str, surname: str, role: str, password: str, email: str, id: Optional[str] = None):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.surname = surname
        self.role = role
        self.password = password
        self.email = email

    def __str__(self):
        return f"{self.role.title()}: {self.name} {self.surname} (ID: {self.id})"


class Tutor(User):
    def __init__(self, name: str, surname: str, password: str, email: str, subject: Optional[str] = None, id: Optional[str] = None):
        super().__init__(name, surname, role='tutor', password=password, email=email, id=id)
        self.subject = subject

    def __str__(self):
        return f"Tutor: {self.name} {self.surname} (Subject: {self.subject}) (ID: {self.id})"


class Student(User):
    def __init__(self, name: str, surname: str, password: str, email: str, grade: Optional[str] = None, id: Optional[str] = None):
        super().__init__(name, surname, role='student', password=password, email=email, id=id)
        self.grade = grade

    def __str__(self):
        return f"Student: {self.name} {self.surname} (Grade: {self.grade}) (ID: {self.id})"
