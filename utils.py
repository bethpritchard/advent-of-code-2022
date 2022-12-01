def file_to_array(file):
    array = []
    with open(file) as input_file:
        for line in input_file:
            line = line.strip()
            array.append(int(line) if line != "" else None)

    return array