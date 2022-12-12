from util import *


def get_normalized_input(inp: list[str]) -> list[str]:
    norm_dict = {
        "A": "ROCK",
        "B": "PAPER",
        "C": "SCISSORS",
        "X": "ROCK",
        "Y": "PAPER",
        "Z": "SCISSORS",
    }
    out = list(map(lambda x: x.split(), inp))
    for (index, item) in enumerate(out):
        out[index] = list(map(lambda x: norm_dict[x], item))
    return out


def main():
    inp = read_input_from_file("input.txt")
    norm_inp = get_normalized_input(inp)
    # Do something with input
    scores = list(map(lambda x: play_round(*x), norm_inp))
    print(norm_inp)
    print(scores)
    # print sum of scores
    print(sum(map(lambda x: x[0], scores)), sum(map(lambda x: x[1], scores)))


if __name__ == '__main__':
    main()
