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


def find_top_three(total_cals):
    total_cals.sort(reverse=True)
    return sum(total_cals[:3])


if __name__ == "__main__":
    totals = count_calories(file_to_array("input.txt"))

    print("Max cals ", max(totals),)

    print("Top three", find_top_three(totals))
