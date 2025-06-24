from oop.university.interfaces import UserInputAdapterInterface


class TerminalInputAdapter(UserInputAdapterInterface):
    def get_user_data(self) -> dict:
        print("Enter user details:")
        name = input("Name: ")
        surname = input("Surname: ")
        role = input("Role (tutor/student): ").lower()
        password = input("Password: ")
        email = input("Email: ")

        user_data = {
            "name": name,
            "surname": surname,
            "role": role,
            "password": password,
            "email": email
        }

        if role == 'tutor':
            subject = input("Subject: ")
            user_data['subject'] = subject
        elif role == 'student':
            grade = input("Grade: ")
            user_data['grade'] = grade

        return user_data

    def get_users_data_bulk(self) -> list:
        print("Bulk input from terminal is not supported.")
        return []
