import math
# parse expressions like:
# new = old * 19
# new = old + 19
# new = old * old


def parseExpression(expression: str):
    # split expression into parts
    parts = expression.split(' ')
    # get the operation
    operation = parts[1]
    # get the first operand
    firstOperand = parts[2]
    # get the second operand
    secondOperand = parts[3]
    # get the third operand
    thirdOperand = parts[4]
    # return a lambda function
    return lambda old: eval(f'{firstOperand} {secondOperand} {thirdOperand}')


def readFromFile(filename: str) -> list:
    with open(filename) as f:
        content = f.readlines()
        # map removes \n
        return list(map(lambda s: s.strip(), content))


class Item:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'


class Monkey:

    def __init__(self, id: int, items: list[Item], operation: str, divTest: int, ifTrueTo: int, ifFalseTo: int):
        self.id = id
        self.inspections = 0
        self.items = items
        self.operation = operation
        self.divTest = divTest
        self.ifTrueTo = ifTrueTo
        self.ifFalseTo = ifFalseTo

    def start(self, pod):
        # calculate item values
        for item in self.items:
            value = parseExpression(self.operation)(item.value)
            value = value % pod
            item.value = value
            self.inspections += 1

        # calculate swaps
        swaps = []
        while (len(self.items) > 0):
            item = self.items.pop()
            if item.value % self.divTest == 0:
                # append tuple of item and monkey id
                swaps.append((item, self.ifTrueTo))
            else:
                swaps.append((item, self.ifFalseTo))
        return swaps

    def __str__(self) -> str:
        out = f'Monkey {self.id}: {", ".join(str(item) for item in self.items)}; '
        out += f'inspections: {self.inspections}'
        return out


def parseMonkey(input: list) -> list:
    monkeys = []
    for i, line in enumerate(input):
        if line.startswith('Monkey'):
            id = int(line[7:8])
            items = list(
                map(lambda x: Item(int(x)), input[i + 1][16:].split(', ')))
            operation = input[i + 2][11:]
            divTest = int(input[i + 3].split(' ')[-1])
            ifTrueTo = int(input[i + 4][-1])
            ifFalseTo = int(input[i + 5][-1])
            monkey = Monkey(id, items, operation, divTest, ifTrueTo, ifFalseTo)
            monkeys.append(monkey)

    return monkeys


def processSwaps(swaps: list[(Item, int)], monkeys: list):
    for (item, id) in swaps:
        monkeys[id].items.append(item)


def doRound(monkeys: list, productOfDivisors: int) -> None:
    for monkey in monkeys:
        swaps = monkey.start(productOfDivisors)
        processSwaps(swaps, monkeys)


def calculateMonkeyBusiness(monkeys: list) -> int:
    monkeys.sort(key=lambda monkey: monkey.inspections, reverse=True)
    return monkeys[0].inspections * monkeys[1].inspections


def main():
    input = readFromFile('input.txt')
    monkeys = parseMonkey(input)
    monkeys = sorted(monkeys, key=lambda monkey: monkey.id)

    productOfDivisors = math.prod(monkey.divTest for monkey in monkeys)

    for i in range(10000):
        if i % 50 == 0:
            print(f'Round {i}')
        doRound(monkeys, productOfDivisors)

    for monkey in monkeys:
        print(monkey)
    print(f'Monkey Business: {calculateMonkeyBusiness(monkeys)}')


if __name__ == '__main__':
    main()
