from refueling import convert
from refueling import validate_fraction
from refueling import gauge
import pytest

def test_convert_valid_fraction():
    assert convert("1/4") == 25
    assert convert("99/100") == 99
    assert convert("1/100") == 1
    assert convert("1/2") == 50

def test_convert_zeroDivision():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_convert_ValueError():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_convert_bigger_numerator():
    with pytest.raises(ValueError):
        validate_fraction("5/3")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(55) == "55%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"