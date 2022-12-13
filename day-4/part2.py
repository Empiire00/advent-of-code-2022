import utils


def is_overlapping(a: (int, int), b: (int, int)) -> bool:
    x1, x2 = a
    y1, y2 = b
    max_x = max(x1, x2)
    min_x = min(x1, x2)
    max_y = max(y1, y2)
    min_y = min(y1, y2)
    # overlapping if min_y <= max_x
    if max_x >= min_y >= min_x:
        return True
    # overlapping if min_x <= max_y
    if max_y >= min_x >= min_y:
        return True
    return False


def main():
    inp = utils.get_file_contents('input.txt')
    lines = [utils.parse_line(x) for x in inp]
    intersecting = list(map(lambda x: is_overlapping((x[0], x[1]), (x[2], x[3])), lines))
    intersecting_intervals = [line for (line, line_intersecting) in zip(lines, intersecting) if line_intersecting]
    print(sum(1 for _ in intersecting_intervals))


if __name__ == '__main__':
    main()
