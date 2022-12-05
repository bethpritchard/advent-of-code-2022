def file_to_array(file):
    array = []
    with open(file) as input_file:
        for line in input_file:
            line = line.strip()
            array.append(int(line) if line != "" else None)

    return array

def read_lines(file):
    with open(file) as input_file:
        return input_file.read().splitlines()
