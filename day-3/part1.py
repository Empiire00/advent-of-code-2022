def read_input_from_file(filename: str)-> list[str]:
    with open(filename) as f:
        out = f.readlines()
        out = [x.strip() for x in out]
        return out


def get_priority(item: str)-> int:
    # a = 1, b = 2, c = 3, ... A = 27, B = 28, C = 29, ...
    if item.isupper():
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1


def main():
    backpacks = read_input_from_file("input.txt")
    # filter out duplicates in each backpack
    duplicates = [set(item for item in backpack[int(len(backpack)/2):] if item in backpack[:int(len(backpack)/2)]) for backpack in backpacks]
    priorities = list(map(lambda x: list(map(get_priority, x)), duplicates))
    priorities = list(map(lambda x: sum(x), priorities))
    priority_sum = sum(priorities)
    print(priority_sum)


if __name__ == "__main__":
    main()
