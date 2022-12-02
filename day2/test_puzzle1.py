from day2.puzzle1 import count_wins


def test_puzzle1():
    expected = 15
    actual = count_wins("test.txt")
    assert actual == expected
