import numpy as np
from utils import *


def drop_sand_infinite(grid: npt.ArrayLike, source: (int, int), max_y: int):
    resting_counter = 0
    still_dropping = True
    while still_dropping:
        resting_counter += 1
        still_dropping = drop_sand(grid, source, max_y)
    return resting_counter


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
    draw(grid, sand_source)
    print()

    print(f'Rested {resting_counter} sand particles')


if __name__ == "__main__":
    main()
