import os
import json


expenses_file = os.path.join(os.path.dirname(__file__), "..", "..", "expenses.json")

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
    with open(expenses_file, "w") as file:
        json.dump(expenses, file, indent=2)


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
