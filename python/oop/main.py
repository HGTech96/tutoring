# cli.py
from oop.university.input.csv_input import CSVInputAdapter
from oop.university.input.terminal_input import TerminalInputAdapter
from oop.university.output.csv_storage import CSVStorageAdapter
from oop.university.services import UserService


def main():
    print("Welcome to User Management CLI!")
    input_method = input("Select input method (terminal/csv): ").strip().lower()

    if input_method == 'terminal':
        input_adapter = TerminalInputAdapter()
    elif input_method == 'csv':
        file_path = input("Enter CSV file path: ").strip()
        input_adapter = CSVInputAdapter(file_path)
    else:
        print("Invalid input method selected.")
        return

    storage_adapter = CSVStorageAdapter('output_users.csv')
    user_service = UserService(input_adapter, storage_adapter)

    if input_method == 'terminal':
        created_user = user_service.create_and_store_single_user()
        print(f"User created: {created_user}")
    elif input_method == 'csv':
        created_users = user_service.create_and_store_bulk_users()
        print(f"{len(created_users)} users created and saved to storage.")


if __name__ == "__main__":
    main()
