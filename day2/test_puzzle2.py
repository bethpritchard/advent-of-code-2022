from day2.puzzle2 import count_score


def test_puzzle2():
    expected = 12
    actual = count_score("test.txt")
    assert actual == expected
