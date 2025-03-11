from seasons import date_to_mins, mins_inflect
import pytest

#test for ValueError
def test_date_to_mins_Sysexit():
    with pytest.raises(SystemExit):
        date_to_mins("03-07-1993")
    with pytest.raises(SystemExit):
        date_to_mins("asdsa")
    with pytest.raises(SystemExit):
        date_to_mins("1993-07-2.5")
