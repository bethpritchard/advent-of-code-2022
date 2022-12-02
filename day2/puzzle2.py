from utils import read_lines


def count_score(file):
    results = read_lines(file)
    score = 0
    for result in results:
        if "Z" in result:
            score += calculate_win(result)
        elif "Y" in result:
            score += calculate_draw(result)
        else:
            score += calculate_loss(result)
    return score


def calculate_win(result):
    score = 6
    if "A" in result:
        score += 2
    elif "B" in result:
        score += 3
    else:
        score += 1
    return score


def calculate_draw(result):
    score = 3
    if "A" in result:
        score += 1
    elif "B" in result:
        score += 2
    else:
        score += 3
    return score


def calculate_loss(result):
    score = 0
    if "A" in result:
        score += 3
    elif "B" in result:
        score += 1
    else:
        score += 2
    return score


if __name__ == "__main__":
    print(count_score("input.txt"))
