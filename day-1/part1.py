
import math


def readFromFile(filename) -> list[str]:
    with open(filename, 'r') as f:
        out = f.readlines()
        out = list(map(lambda x: x.strip(), out))
        return out


def main():
    input = readFromFile('input.txt')
    print(input)

    elves = [[]]
    currElf = 0
    for line in input:
        if len(line) == 0:
            currElf += 1
            elves.append([])
        else:
            elves[currElf].append(int(line))

    elves = list(map(lambda x: sum(x), elves))
    elves.sort(reverse=True)
    print(elves[0])


if __name__ == '__main__':
    main()
