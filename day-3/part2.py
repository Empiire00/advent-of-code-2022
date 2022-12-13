def read_input_from_file(filename: str) -> list[str]:
    with open(filename) as f:
        out = f.readlines()
        out = [x.strip() for x in out]
        return out


def get_groups(backpacks: list[str]) -> list[list[str]]:
    groups = []
    for i in range(0, len(backpacks), 3):
        groups.append(backpacks[i:i + 3])
    return groups


def get_priority(item: str) -> int:
    # a = 1, b = 2, c = 3, ... A = 27, B = 28, C = 29, ...
    if item.isupper():
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1


def main():
    backpacks = read_input_from_file("input.txt")
    # filter out duplicates in each backpack
    groups = get_groups(backpacks)
    badge_priority_sum = 0
    for group in groups:
        badge = list(set(item for item in group[0] if item in group[1] and item in group[2]))[0]
        badge_priority = get_priority(badge)
        badge_priority_sum += badge_priority
    print(badge_priority_sum)


if __name__ == "__main__":
    main()
