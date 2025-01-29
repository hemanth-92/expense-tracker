import os
import json


expenses_file = "expenses.json"

def read_expenses():
    if not os.path.exists(expenses_file):
        return []
    try:
        with open(expenses_file, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("The json data is corrupted")


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
