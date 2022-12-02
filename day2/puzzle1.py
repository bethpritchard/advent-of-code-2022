from utils import read_lines

WINS = ["A Y", "B Z", "C X"]
DRAWS = ["A X", "B Y", "C Z"]


def count_wins(file):
    results = read_lines(file)
    score = 0
    for result in results:
        if result in WINS:
            score +=6
        elif result in DRAWS:
            score += 3
        if "X" in result:
             score += 1
        elif "Y" in result:
            score += 2
        elif "Z" in result:
            score += 3
    return score


if __name__ == "__main__":
    print(count_wins("input.txt"))
