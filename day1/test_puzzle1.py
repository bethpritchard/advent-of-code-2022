from day1.puzzle1 import count_calories, find_top_three
from utils import file_to_array

TEST_INPUT = file_to_array("day_1_test.txt")


def test_calorie_count():
    expected = [6000,4000,11000,24000,10000]
    actual = count_calories(TEST_INPUT)
    assert actual == expected


def test_top_three():
    cal_array = [6000,4000,11000,24000,10000]
    expected = 24000+11000+10000
    actual = find_top_three(cal_array)
    assert actual == expected
