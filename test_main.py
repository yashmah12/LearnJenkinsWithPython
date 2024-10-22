import pytest
from main import *

def test_add_positive_numbers():
    assert add(3, 5) == 8

def test_add_negative_numbers():
    assert add(-1, -2) == -3

def test_add_zero():
    assert add(0, 5) == 5

def test_add_floats():
    assert add(2.5, 3.1) == pytest.approx(5.6)  # Using approx for floating-point precision
