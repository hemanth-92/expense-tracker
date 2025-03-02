import pytest
from commands.summary import expenses_summary
from unittest.mock import patch


@pytest.fixture
def mock_expenses():
  return[
    {"date": "2024-01-15", "amount": 1000.00, "description": "Test 1"},
    {"date": "2024-02-20", "amount": 2000.00, "description": "Test 2"},
    {"date": "2024-02-25", "amount": 3000.00, "description": "Test 3"},
  ]

def test_no_expenses(capsys):
  with patch('commands.summary.read_expenses',return_value=[]):
    expenses_summary()
    captured = capsys.readouterr()
    assert "No expenses found" in captured.out


def test_summary_all_month(mock_expenses,capsys):
  with patch("commands.summary.read_expenses",return_value=mock_expenses):
    result = expenses_summary()
    captured = capsys.readouterr()
    assert result is True
    assert "Rs 6,000.00" in captured.out

def test_summary_specific_month(mock_expenses,capsys):
  with patch("commands.summary.read_expenses",return_value=mock_expenses):
    result  = expenses_summary(month=2)
    captured = capsys.readouterr()
    assert result is True
    assert "February" in captured.out

def test_expenses_month_no_expenses(mock_expenses,capsys):
  with patch("commands.summary.read_expenses",return_value=mock_expenses):
    result = expenses_summary(month=3)
    captured = capsys.readouterr()
    assert result is False
    assert "March" in captured.out
    assert "No expenses found" in captured.out