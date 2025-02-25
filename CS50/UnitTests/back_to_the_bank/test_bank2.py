from bank2 import value

def test_value_if_int():
    assert value("123123") == "$100" 

def test_value_if_hello():
    assert value("hello") == "$0"

def test_value_if_startwith_H():
    assert value("hey") == "$20"

def test_value_default_case():
    assert value("what's up") == "$100"

def test_value_case_insensitive():
    assert value("HEY") == "$20"