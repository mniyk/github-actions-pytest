import pytest
from calculator import add, subtract, multiply, divide, sum_evens

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

def test_sum_evens():
    assert sum_evens([1, 2, 3, 4, 5, 6]) == 12

def test_sum_evens_empty():
    assert sum_evens([]) == 0

