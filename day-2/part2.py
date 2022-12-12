from util import *


# rock paper scissors
# "A": rock
# "B": paper
# "C": scissors
def get_normalized_input(inp: list[str]) -> list[str]:
    norm_dict = {
        "A": "ROCK",
        "B": "PAPER",
        "C": "SCISSORS",
        "X": "LOSE",
        "Y": "DRAW",
        "Z": "WIN",
    }
    out = list(map(lambda x: x.split(), inp))
    for (index, item) in enumerate(out):
        out[index] = list(map(lambda x: norm_dict[x], item))
    return out


def get_move_with_outcome(p1, outcome) -> str:
    outcome_dict = {
        "ROCK": {"WIN": "PAPER", "DRAW": "ROCK", "LOSE": "SCISSORS"},
        "PAPER": {"WIN": "SCISSORS", "DRAW": "PAPER", "LOSE": "ROCK"},
        "SCISSORS": {"WIN": "ROCK", "DRAW": "SCISSORS", "LOSE": "PAPER"}
    }
    return outcome_dict[p1][outcome]


def main():
    inp = read_input_from_file("input.txt")
    norm_inp = get_normalized_input(inp)
    # calculate moves
    moves = list(map(lambda x: [x[0], get_move_with_outcome(x[0], x[1])], norm_inp))

    scores = list(map(lambda x: play_round(*x), moves))
    print(norm_inp)
    print(moves)
    print(scores)
    # print sum of scores
    print(sum(map(lambda x: x[0], scores)), sum(map(lambda x: x[1], scores)))


if __name__ == '__main__':
    main()