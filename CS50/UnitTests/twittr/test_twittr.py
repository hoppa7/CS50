from twttr import shorten

def test_shorten_novowels():
        assert shorten("apple") == "ppl"
        assert shorten("banana") == "bnn"

def test_shorten_numbers():
        assert shorten("12345") == "12345"

def test_shorten_empty_string ():
        assert shorten("") == ""

def test_shorten_capital_letters():
        assert shorten("PYTHON") == "PYTHN"

def test_shorten_letters_n_nums():
        assert shorten("apple12345") == "ppl12345"

def test_shorten_all_vowels():
        assert shorten("AEIOUaeiou") == ""

