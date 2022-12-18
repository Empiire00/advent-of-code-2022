from utils import *


def main() -> None:
    inp = load_input_file("input.txt")
    unique_chars = get_unique_chars(inp, 14)
    position = inp.find(unique_chars)
    print(f' Result "{unique_chars}" at position {position}')


if __name__ == "__main__":
    main()
