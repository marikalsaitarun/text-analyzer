from app import calculate_future_age


def test_calculate_future_age():
    assert calculate_future_age(25) == 30
    assert calculate_future_age(30) == 35