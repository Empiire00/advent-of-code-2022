import numpy as np
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


def drop_sand_infinite(grid: npt.ArrayLike, source: (int, int), max_y: int):
    resting_counter = 0
    still_dropping = True
    while still_dropping:
        resting_counter += 1
        still_dropping = drop_sand(grid, source, max_y)
    return resting_counter


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


def draw(grid: npt.ArrayLike, min_x: int, max_x: int, min_y: int, max_y: int):
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            # print an o if there is sand
            # print a ' if there is nothing
            # print a # if there is a rock
            if grid[y, x] == "S":
                print("o", end="")
            elif grid[y, x] == "R":
                print("#", end="")
            else:
                print("'", end="")

        print()


def main() -> None:
    inp = read_from_file("input.txt")
    sand_source = (500, 0)
    rock_coordinates = get_rock_coordinates(inp)
    """
    ............O\...........   0
    ...........o|o\..........   1
    ..........oo|oo\.........   2
    .........ooo|ooo\........   3
    ........oo#o|o##o\.......   4
    .......ooo#o|o#ooo\......   5
    ......oo###o|o#oooo\.....   6
    .....oooo.oo|o#ooooo\....   7
    ....oooooooo|o#oooooo\...   8
    ...ooo######|##ooooooo\..   9
    ..ooooo.....|.ooooooooo\.   A
    ############|############## B
                0 2 4 6 8 A C 
                
    One can see, that the sand is forming a triangle, which is resting on the infinite rock.
    Therefore, we do only need to check as many x values to the left and right of the source as the triangle is wide.
    right side: 
        max_x_infinite_rock = max_x + dist(y_source, y of infinite rock) + 1
    left side:
        min_x_infinite_rock = min_x - dist(y_source, y of infinite rock) - 1
    """
    _, max_x, _, max_y = get_min_max([(x, y, "R") for x, y in rock_coordinates])

    # get position for "infinite rock"
    y_infinite_rock = max_y + 2
    y_dist = y_infinite_rock - sand_source[1]
    # get x values of infinite rock
    max_x_infinite_rock = sand_source[0] + y_dist + 1
    min_x_infinite_rock = sand_source[0] - y_dist - 1
    possible_x_values = range(min_x_infinite_rock, max_x_infinite_rock + 1)
    possible_y_values = range(0, y_infinite_rock + 1)
    rock_coordinates.extend([(x, y_infinite_rock) for x in possible_x_values])

    grid = np.empty((len(possible_y_values), len(possible_x_values)), dtype=object)
    grid[:] = "'"
    # fill grid with rocks
    for x, y in rock_coordinates:
        grid[y, x - min_x_infinite_rock] = "R"
    # fill grid with sand
    # map sand source to grid
    sand_source = (sand_source[0] - min_x_infinite_rock, sand_source[1])
    resting_counter = drop_sand_infinite(grid, sand_source, y_infinite_rock)
    draw(grid, 0, len(possible_x_values) - 1, 0, len(possible_y_values) - 1)

    print(f'Rested {resting_counter} sand particles')


if __name__ == "__main__":
    main()
