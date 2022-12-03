from day3.puzzle1 import count_items
from utils import read_lines


def find_common_letter(rucksacks):
    first_common = list(set([item for item in rucksacks[0] if item in rucksacks[1]]))
    return list(set([item for item in first_common if item in rucksacks[2]]))[0]


def find_total_score(file):
    rucksacks = read_lines(file)
    score = 0
    for i in range(0,len(rucksacks)//3):
        score += count_items(find_common_letter(rucksacks[i*3:(i*3)+3]))
    return score

if __name__ == "__main__":
    print(find_total_score("input.txt"))