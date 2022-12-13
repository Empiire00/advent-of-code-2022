from utils import *


def move(amount: int, from_stack: int, to_stack: int, stacks: list[list[str]]):
    """move a given amount of blocks from one stack to another. All at once
    :param amount: amount of containers to move
    :param from_stack: stack to move from
    :param to_stack: stack to move to
    :param stacks: list of stacks
    :return: None
    """
    index_from, index_to = from_stack - 1, to_stack - 1
    crane_holds = []
    for i in range(amount):
        crane_holds.append(stacks[index_from].pop())
    crane_holds.reverse()
    # append crane_holds to target stack
    stacks[index_to].extend(crane_holds)


def main():
    inp = read_file("input.txt")
    stack_lines, movements = split_input(inp)
    stacks = parse_stack_lines(stack_lines)
    moves = [parse_move(x) for x in movements]
    for mv in moves:
        move(*mv, stacks)
    # get last element of each stack
    last_elements = [re.sub(r'[][]', "", x[-1]) for x in stacks]
    print("Result: " + "".join(last_elements), end="\n\n")
    print_stacks(stacks)


if __name__ == "__main__":
    main()
