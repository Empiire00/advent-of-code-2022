from utils import *
import numpy as np


def main() -> None:
    inp = read_from_file("input.txt")
    # coordinates (x, y)
    sand_source = (500, 0)
    rock_coordinates = get_rock_coordinates(inp)

    # use utils to find out the amount of dropped sand
    min_x, max_x, min_y, max_y = get_min_max([(x, y, "R") for x, y in rock_coordinates])
    possible_x = [x for x in range(min_x, max_x + 1)]
    possible_y = [y for y in range(max_y + 1)]
    grid = np.empty((len(possible_y), len(possible_x)), dtype=object)
    grid[:] = "'"
    # fill grid with rocks
    for x, y in rock_coordinates:
        grid[y, x - min_x] = "R"
    # fill grid with sand
    # map sand source to grid
    sand_source = (sand_source[0] - min_x, sand_source[1])
    rested = 0
    while drop_sand(grid, sand_source, max_y):
        # draw(grid, sand_source)
        rested += 1
    draw(grid, sand_source)
    print()
    print(f'Rested {rested} sand particles')


if __name__ == "__main__":
    main()
