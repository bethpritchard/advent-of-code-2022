from day3.puzzle2 import find_common_letter, find_total_score


def test_common_letter():
    input = ["vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg"]
    expected = "r"
    actual = find_common_letter(input)
    assert actual == expected


def test_total_score():
    actual = find_total_score("test.txt")
    expected = 70
    assert actual == expected