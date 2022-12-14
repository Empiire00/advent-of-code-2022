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

def drop_sand(grid: list[(int, int, str)], source: (int, int), max_y: int) -> bool:
    dropping = True
    (posX, posY) = source
    while dropping and posY < max_y:
        # try to move down
        if (posX, posY + 1, "S") not in grid and (posX, posY + 1, "R") not in grid:
            posY += 1
        # try to move left down
        elif (posX - 1, posY + 1, "S") not in grid and (posX - 1, posY + 1, "R") not in grid:
            posX -= 1
            posY += 1
        # try to move right down
        elif (posX + 1, posY + 1, "S") not in grid and (posX + 1, posY + 1, "R") not in grid:
            posX += 1
            posY += 1
        # rest on current position
        else:
            dropping = False
            grid.extend([(posX, posY, "S")])
            return True
    return False


def get_min_max(grid: list[(int, int, str)]) -> (int, int, int, int):
    """
    Returns (x_min, x_max, y_min, y_max)
    :param rock_coordinates:
    :return: tuple (x_min, x_max, y_min, y_max)
    """
    min_x = min(grid, key=lambda x: x[0])[0]
    max_x = max(grid, key=lambda x: x[0])[0]
    min_y = min(grid, key=lambda x: x[1])[1]
    max_y = max(grid, key=lambda x: x[1])[1]
    return min_x, max_x, min_y, max_y


def draw(grid: list[(int, int, str)], sand_source: (int, int)) -> None:
    min_x, max_x, min_y, max_y = get_min_max(grid)
    min_y = min(min_y, sand_source[1])
    for y in range(min_y -1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            if (x, y) == sand_source:
                print("+", end="")
            elif (x, y, "R") in grid:
                print("#", end="")
            elif (x, y, "S") in grid:
                print("o", end="")
            else:
                print("´", end="")
        print()


def main() -> None:
    inp = read_from_file("test.txt")
    # coordinates (x, y)
    sand_source = (500, 0)
    rock_coordinates = get_rock_coordinates(inp)
    grid = [(x, y, "R") for x,y in rock_coordinates]
    min_x, max_x, min_y, max_y = get_min_max(grid)
    draw(grid, sand_source)
    rested = 0
    while drop_sand(grid, sand_source, max_y):
        # draw(grid, sand_source)
        rested += 1
    draw(grid, sand_source)
    print(f'Rested {rested} sand particles')

if __name__ == "__main__":
    main()
