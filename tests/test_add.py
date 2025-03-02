from commands.add import add_expenses
import pytest

@pytest.mark.parametrize("description, amount, expected", [
    ("Lunch", 100, True),
    ("Coffee", 5.50, True),

    ("Negative", -100, False),
    ("Zero", 0, False),
    ("Invalid number", "abc", False),
    
    ("", 100, False),  # Empty description
    (None, 100, False),  # None description
])
def test_add_expenses_parametrized(description, amount, expected):
    result = add_expenses(description, amount)
    assert result is expected