from simple_interest import simple_interest


def test_normal():
    assert simple_interest(10000, 5, 2) == 1000


def test_zero_rate():
    assert simple_interest(10000, 0, 2) == 0


def test_zero_time():
    assert simple_interest(10000, 5, 0) == 0


def test_decimal():
    assert simple_interest(1000, 2.5, 2) == 50