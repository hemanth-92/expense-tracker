from commands.list import list_expenses
import pytest
from unittest.mock import patch

def test_list_expenses_empty(capsys):
    with patch('commands.list.read_expenses',return_value=[]):
        list_expenses()
        captured = capsys.readouterr()
        assert captured.out.strip() == '[]'

def test_list_expenses_with_data(capsys):
        sample_expenses = [
        {'amount': 50.0, 'category': 'food', 'date': '2024-03-20', 'description': 'Groceries'},
        {'amount': 30.0, 'category': 'transport', 'date': '2024-03-21', 'description': 'Bus fare'}
    ]
        with patch('commands.list.read_expenses',return_value=sample_expenses):
            list_expenses()
            captured = capsys.readouterr()
            assert captured.out.strip() == str(sample_expenses)