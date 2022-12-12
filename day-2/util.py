def read_input_from_file(filename: str) -> list[str]:
    with open(filename, "r") as file:
        out = file.readlines()
        return list(map(lambda x: x.strip(), out))


def get_move_score(move: str) -> int:
    score_dict = {
        "ROCK": 1,
        "PAPER": 2,
        "SCISSORS": 3,
    }
    return score_dict[move]


def get_result(p1: str, p2: str) -> (int, int):
    win_dict = {
        "ROCK": {"ROCK": 3, "PAPER": 0, "SCISSORS": 6},
        "PAPER": {"ROCK": 6, "PAPER": 3, "SCISSORS": 0},
        "SCISSORS": {"ROCK": 0, "PAPER": 6, "SCISSORS": 3}
    }
    return win_dict[p1][p2], win_dict[p2][p1]


def play_round(player1: str, player2: str) -> (int, int):
    p1 = get_move_score(player1)
    p2 = get_move_score(player2)
    (points1, points2) = get_result(player1, player2)
    return points1 + p1, points2 + p2
