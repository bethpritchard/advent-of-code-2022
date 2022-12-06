from utils import read_lines

def find_letters(letters, msg_type):
    marker_size = 0
    if msg_type == "packet":
        marker_size=4
    elif msg_type == "message":
        marker_size=14
    for i in range(len(letters)-marker_size):
        substring = letters[i:i+marker_size]
        set_substring = list(set(substring))
        if len(substring) == len(set_substring):
            return i+marker_size


def get_array(file):
    return [letter for letter in read_lines(file)[0]]


if __name__ == "__main__":
   print("Part 1: ", find_letters(get_array("input.txt"), "packet"))
   print("Part 2: ", find_letters(get_array("input.txt"), "message"))