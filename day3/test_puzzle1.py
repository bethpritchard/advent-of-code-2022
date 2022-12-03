from day3.puzzle1 import count_items, find_similar_items, count_rucksacks


def test_count_items():
    input = "p"
    expected = 16
    actual = count_items(input)
    assert actual == expected


def test_find_similar_items():
    input = "vJrwpWtwJgWrhcsFMMfFFhFp"
    expected = "p"
    actual = find_similar_items(input)
    assert actual == expected


def test_count_rucksacks():
    actual = count_rucksacks("test.txt")
    expected = 157
    assert actual == expected
