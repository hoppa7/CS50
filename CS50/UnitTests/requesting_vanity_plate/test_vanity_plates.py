from vanity_plates2 import is_valid

def test_valid_negative_int():
    assert is_valid("-1") == False

def test_valid_case_insensitive_and_length():
    assert is_valid("CSA513") == True
    assert is_valid("cssA0010") == False

def test_valid_only_int():
    assert is_valid("123214") == False

def test_numbers_middle():
    assert is_valid("CSS503") == True
    assert is_valid("CS50A3") == False

def test_valid_punctuation_plus_specialChars():
    assert is_valid("AA1,2") == False
    assert is_valid("??!?!?#$%") == False

def test_valid_zero_in_middle():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

def test_startsWith_2letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False

