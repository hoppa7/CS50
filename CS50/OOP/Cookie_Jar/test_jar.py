import pytest
from jar import Jar
def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "Cookie Cookie Cookie "

    with pytest.raises(ValueError):
        jar.deposit(13)

def test_deposit():
    jar = Jar(10)

    jar.deposit(2)
    assert str(jar) == "Cookie Cookie "

    with pytest.raises(ValueError):
        jar.deposit(9)

def test_withdraw():
    jar = Jar(10)

    jar.deposit(7)
    jar.withdraw(2)
    assert str(jar) == "Cookie Cookie Cookie Cookie Cookie "

    with pytest.raises(ValueError):
        jar.withdraw(6)