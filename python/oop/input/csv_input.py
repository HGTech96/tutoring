import csv

from oop.university.interfaces import UserInputAdapterInterface


class CSVInputAdapter(UserInputAdapterInterface):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_user_data(self) -> dict:
        raise NotImplementedError("CSV input adapter only supports bulk reading.")

    def get_users_data_bulk(self) -> list:
        users = []
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append(row)
        return users
