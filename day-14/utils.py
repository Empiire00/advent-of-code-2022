import numpy.typing as npt


def read_from_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        out = f.readlines()
        return [line.strip() for line in out]


def parse_rock_data(line: str) -> list[(int, int)]:
    # groups = [[x1, y1 for (x1,y1) in zip(x.strip().split(",") for x in line.split("->")) ]
    groups = [x.strip().split(",") for x in line.split("->")]
    rocks = []

    first = groups[0]
    for i in groups[1:]:
        second = i
        # get occupied coordinates
        x_min = min(int(first[0]), int(second[0]))
        x_max = max(int(first[0]), int(second[0]))
        y_min = min(int(first[1]), int(second[1]))
        y_max = max(int(first[1]), int(second[1]))
        x_range = [x for x in range(x_min, x_max + 1) or [int(first[0])]]
        y_range = [y for y in range(y_min, y_max + 1) or [int(first[1])]]
        rocks.extend([(x, y) for x in x_range for y in y_range])
        first = second
    return rocks


def get_rock_coordinates(data: list[str]) -> list[(int, int)]:
    rocks = [parse_rock_data(line) for line in data]
    flattened_rocks = [item for sublist in rocks for item in sublist]
    rock_coordinates = list(map(lambda rock: (rock[0], rock[1]), flattened_rocks))
    return rock_coordinates


def get_min_max(grid: list[(int, int, str)]) -> (int, int, int, int):
    """
    Returns (x_min, x_max, y_min, y_max)
    :param grid:
    :return: tuple (x_min, x_max, y_min, y_max)
    """
    min_x = min(grid, key=lambda x: x[0])[0]
    max_x = max(grid, key=lambda x: x[0])[0]
    min_y = min(grid, key=lambda x: x[1])[1]
    max_y = max(grid, key=lambda x: x[1])[1]
    return min_x, max_x, min_y, max_y


def draw(grid: npt.ArrayLike, source):
    max_y, max_x = grid.shape
    for y in range(max_y):
        for x in range(max_x):
            if grid[y, x] == "S":
                print("o", end="")
            elif grid[y, x] == "R":
                print("#", end="")
            elif (x, y) == source:
                print("+", end="")
            else:
                print("'", end="")
        print()


def drop_sand(grid: npt.ArrayLike, source: (int, int), max_y: int) -> bool:
    (posX, posY) = source
    while posY < max_y:
        # try to move down
        # if there is a rock or sand below, stop
        neighbor_down = grid[posY + 1, posX]
        neighbor_down_left = grid[posY + 1, posX - 1]
        neighbor_down_right = grid[posY + 1, posX + 1]
        if neighbor_down != "R" and neighbor_down != "S":
            posY += 1
            continue
        # try to move left down
        elif neighbor_down_left != "R" and neighbor_down_left != "S":
            posX -= 1
            posY += 1
            continue
        # try to move right down
        elif neighbor_down_right != "R" and neighbor_down_right != "S":
            posX += 1
            posY += 1
            continue
        # rest on current position
        else:
            grid[posY, posX] = "S"
            if (posX, posY) == source:
                break
            return True
    return False