from utils import file_to_array


def count_calories(original_list):
    total_cals = []
    cals = 0
    for i in range(0, len(original_list)):
        if original_list[i] is None:
            total_cals.append(cals)
            cals = 0
        else:
            cals += original_list[i]
    if original_list[-1] is not None:
        total_cals.append(cals)
    return total_cals


def find_max_value(totals):
    max_cals = max(totals)
    index = totals.index(max_cals)
    return max_cals, index

def find_top_three(total_cals):
    top_three = []
    count = 0
    while count < 3:
        top_three.append(max(total_cals))
        total_cals.pop(total_cals.index(max(total_cals)))
        count += 1
    return sum(top_three)

if __name__ == "__main__":
    cals = count_calories(file_to_array("input.txt"))

    max_cals, index = find_max_value(cals)

    print("Cals ", max_cals, "Index ", index)

    print("Top three", find_top_three(cals))

