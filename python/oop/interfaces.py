from abc import ABC, abstractmethod

from python.oop.entities import User


class UserCreatorInterface(ABC):
    @abstractmethod
    def create_user(self, user_data: dict) -> User:
        """Create a single user from provided data."""
        pass

    @abstractmethod
    def create_users_bulk(self, users_data: list[dict]) -> list[User]:
        """Create multiple users from provided data."""
        pass


class UserInputAdapterInterface(ABC):
    @abstractmethod
    def get_user_data(self) -> dict:
        """Get data for a single user."""
        pass

    @abstractmethod
    def get_users_data_bulk(self) -> list[dict]:
        """Get data for multiple users."""
        pass


class UserStorageAdapterInterface(ABC):
    @abstractmethod
    def save_user(self, user: User) -> None:
        """Save a single user to storage."""
        pass

    @abstractmethod
    def save_users_bulk(self, users: list[User]) -> None:
        """Save multiple users to storage."""
        pass
