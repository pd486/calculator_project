import pytest
from calculator import add, subtract, multiply, divide

# --- add ---
def test_add_positive_numbers():
    assert add(3, 4) == 7

def test_add_negative_numbers():
    assert add(-2, -5) == -7

def test_add_with_zero():
    assert add(10, 0) == 10

# --- subtract ---
def test_subtract_basic():
    assert subtract(10, 4) == 6

def test_subtract_gives_negative():
    assert subtract(3, 7) == -4

# --- multiply ---
def test_multiply_basic():
    assert multiply(3, 5) == 15

def test_multiply_by_zero():
    assert multiply(9, 0) == 0

# --- divide ---
def test_divide_basic():
    assert divide(10, 2) == 5

def test_divide_gives_float():
    assert divide(7, 2) == 3.5

def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(5, 0)