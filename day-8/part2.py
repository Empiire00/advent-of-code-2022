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
    scenic_scores = np.zeros(inp.shape)
    for (i, j), val in np.ndenumerate(inp):
        above, below, left, right = 0, 0, 0, 0

        # check how far to see above
        for k in range(i - 1, -1, -1):
            above += 1
            if val <= inp[k, j]:
                break
        # check how far to see below
        for k in range(i + 1, inp.shape[0]):
            below += 1
            if val <= inp[k, j]:
                break
        # check how far to see left
        for k in range(j - 1, -1, -1):
            left += 1
            if val <= inp[i, k]:
                break
        # check how far to see right
        for k in range(j + 1, inp.shape[1]):
            right += 1
            if val <= inp[i, k]:
                break

        scenic_scores[i, j] = above * below * left * right

    print(f'max scenic score: {np.max(scenic_scores)}')


if __name__ == '__main__':
    main()
