from utils import read_lines

def find_overlap(a,b):
    return (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1])

def find_all_overlaps(a,b):
    if  a[0] <= b[0] or a[1] >= b[1]:
        return True
    elif  b[0] <= a[0] or b[1] >= a[1]:
        return True
    else:
        return False

def find_score(file):
    lines = [line.split(',') for line in read_lines(file)]
    score = 0
    for line in [[elf.split('-') for elf in line] for line in lines]:
        a, b = [int(num) for num in line[0]], [int(num) for num in line[1]]
        score += find_overlap(a,b)

    return score


if __name__ == "__main__":
    print(find_score("test.txt"))

