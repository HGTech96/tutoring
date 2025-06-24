# cli.py
from python.oop.input.csv_input import CSVInputAdapter
from python.oop.input.terminal_input import TerminalInputAdapter
from python.oop.output.csv_storage import CSVStorageAdapter
from python.oop.services import UserService


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

    storage_adapter = CSVStorageAdapter('output')
    user_service = UserService(input_adapter, storage_adapter)

    if input_method == 'terminal':
        created_user = user_service.create_and_store_single_user()
        print(f"User created: {created_user}")
    elif input_method == 'csv':
        created_users = user_service.create_and_store_bulk_users()
        print(f"{len(created_users)} users created and saved to storage.")


if __name__ == "__main__":
    main()
