import re


def read_file(filename: str) -> str:
    with open(filename) as f:
        out = f.read()
        return out


def split_input(inp: str) -> (list[str], list[str]):
    stack_lines, movements = inp.split('\n\n')
    stack_lines = stack_lines.splitlines()
    movements = movements.splitlines()
    return stack_lines, movements


def parse_stack_lines(stack_lines: list[str]) -> list[list[str]]:
    last_stack_line = stack_lines[-1]
    last_stack_line = re.split(r'\s+', last_stack_line.strip())
    amount_of_stacks = sum([1 for _ in last_stack_line])
    stacks = [[] for _ in range(amount_of_stacks)]

    for line in stack_lines[-2::-1]:
        for i in range(0, amount_of_stacks, 1):
            start_pos = i * 4
            end_pos = start_pos + 3
            current_line = line[start_pos:end_pos]
            stacks[i].append(current_line)
    # Again, I like this programming language :D
    stacks = [list(filter(lambda item: item.strip() != "", x)) for x in stacks]
    return stacks


def print_stacks(stacks: list[list[str]]) -> None:
    # stacks get printed in reverse order (top to bottom)
    # for simplicity's sake

    max_len = max([len(x) for x in stacks])
    # print stack numbers
    print(" " + "   ".join([str(i) for i in range(1, len(stacks) + 1)]))
    for i in range(max_len):
        for stack in stacks:
            if i >= len(stack):
                print("   ", end=" ")
            else:
                print(stack[i], end=" ")
        print()


def parse_move(move: str) -> (int, int, int):
    """
    :param move:
    :return: tuple (amount, from, to)
    """
    # example for move: "move 1 from 3 to 5"
    result = re.search(r'move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)', move)
    return int(result.group(1)), int(result.group(2)), int(result.group(3))