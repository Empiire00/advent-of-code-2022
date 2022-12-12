import numpy as np


def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        # strip and split at every digit
        lines = [line.strip() for line in lines]
        lines = [[int(x) for x in line] for line in lines]
        return lines


def main():
    inp = read_input("input.txt")
    inp = np.array(inp)
    visibilities = np.zeros(inp.shape)
    visibilities[0, :] = 1
    visibilities[-1, :] = 1
    visibilities[:, 0] = 1
    visibilities[:, -1] = 1
    for (i, j), val in np.ndenumerate(inp):
        if i == 0 or j == 0 or i == inp.shape[0] - 1 or j == inp.shape[1] - 1:
            continue

        # check if all above are smaller
        if np.all(inp[:i, j] < val):
            visibilities[i, j] = 1
            continue
        # check if all below are smaller
        if np.all(inp[i + 1:, j] < val):
            visibilities[i, j] = 1
            continue
        # check if all left are smaller
        if np.all(inp[i, :j] < val):
            visibilities[i, j] = 1
            continue
        # check if all right are smaller
        if np.all(inp[i, j + 1:] < val):
            visibilities[i, j] = 1
            continue
    print(f'{visibilities.sum()}')


if __name__ == '__main__':
    main()
