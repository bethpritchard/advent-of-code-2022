# read file in
# separate into pairs
# get list from the two pairs
# compare lists#
from utils import read_lines


def find_overlap(line):
    a, b = [int(num) for num in line[0]], [int(num) for num in line[1]]
    return (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1])


def find_score(file):
    lines = [line.split(',') for line in read_lines(file)]
    score = 0
    for line in [[elf.split('-') for elf in line] for line in lines]:
        score += find_overlap(line)
    return score


if __name__ == "__main__":
    print(find_score("input.txt"))

