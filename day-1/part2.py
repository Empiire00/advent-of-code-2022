
import math


def readFromFile(filename) -> list[str]:
    with open(filename, 'r') as f:
        out = f.readlines()
        out = list(map(lambda x: x.strip(), out))
        return out


def main():
    input = readFromFile('input.txt')

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
    sumOfTopThree = sum(elves[:3])
    print(sumOfTopThree)


if __name__ == '__main__':
    main()
