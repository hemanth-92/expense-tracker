import pytest
from commands.delete import delete_expenses
from unittest.mock import patch

# Mock data for our tests
MOCK_EXPENSES = [
    {"id": 5, "amount": 100, "description": "Test expense 1"},
    {"id": 11, "amount": 200, "description": "Test expense 2"},
    {"id": 15, "amount": 300, "description": "Test expense 3"}
]

@pytest.mark.parametrize("id,expected,remaining_count", [
    (5, True, 2),
    (11, True, 2),
    ("5", True, 2),
    ("11", True, 2),  
    
    ("", False, 3),
    (None, False, 3),
    (-1, False, 3),
    (999, False, 3),  
    ("invalid", False, 3)
])
def test_delete_expenses(id, expected, remaining_count):
    with patch('commands.delete.read_expenses') as mock_read, \
        patch('commands.delete.write_expenses') as mock_write:

        mock_read.return_value = MOCK_EXPENSES.copy()
        
        result = delete_expenses(id)
        
        assert result is expected
        
        if expected:
            assert len(mock_write.call_args[0][0]) == remaining_count
            remaining_ids = [str(exp["id"]) for exp in mock_write.call_args[0][0]]
            assert str(id) not in remaining_ids