from utils import read_lines


def find_similar_items(rucksack):
    first_half, second_half = rucksack[:(len(rucksack)//2)], rucksack[(len(rucksack)//2):]
    return list(set([item for item in first_half if item in second_half]))[0]


def count_items(item):
    letters = list(map(chr, range(97, 123)))
    # Delightful
    priorities = {**dict(zip(letters, range(1, 27))),
                  **dict(dict((k.upper(), v + 26) for k, v in dict(zip(letters, range(1, 27))).items()))}
    return priorities[item]


def count_rucksacks(file):
    rucksacks = read_lines(file)
    score = 0
    for rucksack in rucksacks:
        score += count_items(find_similar_items(rucksack))
    return score


if __name__ == "__main__":
    print(count_rucksacks("input.txt"))

