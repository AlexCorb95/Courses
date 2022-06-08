import pytest
import factorial_one


def test_factorial():
    result = factorial_one.factorial(5)
    assert result == 120

def test_factorial_negativ():
    result = factorial_one.factorial(-2)
    assert result is None

def test_factorial_zero():
    result = factorial_one.factorial(0)
    assert result == 1

def test_factorial_big():
    result = factorial_one.factorial(10)
    assert result == 3628800