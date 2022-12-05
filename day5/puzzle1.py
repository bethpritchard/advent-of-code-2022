from utils import read_lines
import numpy as np

def get_array(lines):
    num_rows = int(lines[-1][-1])
    lines = lines[:-1]
    arrays = []
    for line in lines:
        new_line = []
        inner_line = line.split("    ")
        for char in inner_line:
            if char == " ":
                new_line.append("None")
            else:
                split_inner = char.split(" ")
                for inner_char in split_inner:
                    if inner_char != "":
                        new_line.append(inner_char)
            if len(new_line) < num_rows:
                new_line.append("None")
        arrays.append(new_line)

    raw_stack =  np.array(arrays).transpose()
    arrays = [np.flip(stack).tolist() for stack in raw_stack]
    trimmed_arrays = []
    for array in arrays:
        trimmed_arrays.append([item for item in array if item != "None"])
    return trimmed_arrays


def get_moves(moves):
    moves_array = []
    for move in moves:
        new_move =[]
        for char in move.split(" "):
            try:
                new_move.append(int(char))
            except ValueError:
                continue

        moves_array.append(new_move)
    return moves_array


def split_input(lines):
    stack, moves = lines[:lines.index("")], lines[lines.index("")+1:]
    return stack, moves


def do_moves(raw_stacks, raw_moves, part):
    stack = get_array(raw_stacks)
    moves = get_moves(raw_moves)

    for move in moves:
        num_to_move = move[0]
        from_col =move[1]-1
        to_col = move[2]-1

        sub_stack = stack[from_col][-num_to_move:]
        if part == 1:
            sub_stack.reverse()
        stack[to_col] += sub_stack
        stack[from_col]=stack[from_col][:-num_to_move]
    return stack


def find_tops(stacks):
    tops = [[inner for inner in stack[-1]] for stack in stacks]
    top_str = ""
    for top in tops:
        top_str += top[1]
    return top_str


def main(file, part):
    stack, moves = split_input(read_lines(file))
    return find_tops(do_moves(stack, moves, part))


if __name__ == "__main__":
    print("Pt1 : ", main("input.txt", part =1))
    print("Pt2 : ", main("input.txt",part=2))
