import pytest
from unittest import mock
from main import *


def test_deposit():
    # Test with valid integer input
    with mock.patch('builtins.input', return_value='100'):
        assert deposit() == 100

    # Test with zero input
    with mock.patch('builtins.input', side_effect=['0', '10']):
        assert deposit() == 10

    # Test with negative input
    with mock.patch('builtins.input', side_effect=['-50', '200']):
        assert deposit() == 200

    # Test with non-integer input
    with mock.patch('builtins.input', side_effect=['hello', '50']):
        assert deposit() == 50


def test_get_number_of_lines():
    # Test with valid integer input
    with mock.patch('builtins.input', return_value='3'):
        assert get_number_of_lines() == 3

    # Test with zero input
    with mock.patch('builtins.input', side_effect=['0', '2']):
        assert get_number_of_lines() == 2

    # Test with negative input
    with mock.patch('builtins.input', side_effect=['-50', '1']):
        assert get_number_of_lines() == 1

    # Test with non-integer input
    with mock.patch('builtins.input', side_effect=['hello', '2']):
        assert get_number_of_lines() == 2


def test_get_bet():
    # Test with valid integer input
    with mock.patch('builtins.input', return_value='20'):
        assert get_bet() == 20

    # Test with zero input
    with mock.patch('builtins.input', side_effect=['0', '2']):
        assert get_bet() == 2

    # Test with negative input
    with mock.patch('builtins.input', side_effect=['-50', '1']):
        assert get_bet() == 1

    # Test with non-integer input
    with mock.patch('builtins.input', side_effect=['hello', '2']):
        assert get_bet() == 2


def test_check_winnings():
    columns = [
        ["A", "B", "D"],
        ["A", "C", "D"],
        ["B", "C", "D"]
    ]
    symbol_value = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2
    }
    bet = 10

    lines = 1
    winnings, winning_lines = check_winnings(columns, lines, bet, symbol_value)
    assert winnings == 0
    assert winning_lines == []

    lines = 2
    winnings, winning_lines = check_winnings(columns, lines, bet, symbol_value)
    assert winnings == 0
    assert winning_lines == []

    lines = 3
    winnings, winning_lines = check_winnings(columns, lines, bet, symbol_value)
    assert winnings == 20
    assert winning_lines == [3]
