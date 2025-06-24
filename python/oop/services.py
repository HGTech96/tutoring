from oop.university.entities import User, Tutor, Student
from oop.university.interfaces import UserCreatorInterface, UserStorageAdapterInterface, UserInputAdapterInterface


class UserFactory:
    @staticmethod
    def create_user(user_data: dict) -> User:
        role = user_data.get('role')
        if role == 'tutor':
            return Tutor(
                name=user_data['name'],
                surname=user_data['surname'],
                password=user_data['password'],
                email=user_data['email'],
                subject=user_data.get('subject')
            )
        elif role == 'student':
            return Student(
                name=user_data['name'],
                surname=user_data['surname'],
                password=user_data['password'],
                email=user_data['email'],
                grade=user_data.get('grade')
            )
        else:
            raise ValueError(f"Unknown user role: {role}")


class UserCreator(UserCreatorInterface):
    def __init__(self, storage_adapter: UserStorageAdapterInterface):
        self.storage_adapter = storage_adapter

    def create_user(self, user_data: dict) -> User:
        user = UserFactory.create_user(user_data)
        self.storage_adapter.save_user(user)
        return user

    def create_users_bulk(self, users_data: list[dict]) -> list[User]:
        users = []
        for user_data in users_data:
            user = UserFactory.create_user(user_data)
            users.append(user)
        self.storage_adapter.save_users_bulk(users)
        return users


# user_management/application/services.py



class UserService:
    def __init__(self, input_strategy: UserInputAdapterInterface, storage_strategy: UserStorageAdapterInterface):
        self.input_strategy = input_strategy
        self.storage_strategy = storage_strategy

    def create_and_store_single_user(self) -> User:
        user_data = self.input_strategy.get_user_data()
        user = UserFactory.create_user(user_data)
        self.storage_strategy.save_user(user)
        return user

    def create_and_store_bulk_users(self) -> list[User]:
        users_data = self.input_strategy.get_users_data_bulk()
        users = []
        for user_data in users_data:
            user = UserFactory.create_user(user_data)
            users.append(user)
        self.storage_strategy.save_users_bulk(users)
        return users
