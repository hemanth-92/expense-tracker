import os
import json


expenses_file =  "expenses.json"

def read_expenses():
    if not os.path.exists(expenses_file):
        return []
    try:
        with open(expenses_file, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: The JSON file is corrupt.")
        user_input = input("Do you want to delete the corrupt file and proceed? (yes/no): ").strip().lower()
        if user_input == 'yes':
            os.remove(expenses_file)
            print("The corrupt file has been deleted. Proceeding with an empty list.")
            return []
        else:
            print("Please delete the corrupt file manually to proceed.")
            exit(1)


def write_expenses(expenses):
    try:
        with open(expenses_file, "w") as file:
            json.dump(expenses, file, indent=2)
    except IOError as e:
        print(f"Error: Failed to write expenses to file: {e}")
        print(f"Make sure you have write permissions to: {expenses_file}")
        exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred while writing expenses: {e}")
        exit(1)


def get_month_text(month):
    return (
        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ][month - 1]
        if month
        else ""
    )
