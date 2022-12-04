from utils import read_lines


def find_overlap(a, b):
    return not (a[1] < b[0] or b[1] < a[0])


def find_score(file):
    lines = [line.split(',') for line in read_lines(file)]
    score = 0
    for line in [[elf.split('-') for elf in line] for line in lines]:
        a, b = [int(num) for num in line[0]], [int(num) for num in line[1]]
        score += find_overlap(a, b)

    return score


if __name__ == "__main__":
    print(find_score("input.txt"))

