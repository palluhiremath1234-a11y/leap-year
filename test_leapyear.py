from leapyear import leapyear

def test_leap():
    assert leapyear(2024) == "Leap Year"

def test_not_leap():
    assert leapyear(2025) == "Not a Leap Year"

def test_zero():
    assert leapyear(2000) == "Leap Year"