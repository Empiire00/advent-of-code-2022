def parse_line(line: str) -> (int, int, int, int):
    x, y = line.split(',')
    x1, x2 = x.split('-')
    y1, y2 = y.split('-')
    return int(x1), int(x2), int(y1), int(y2)


def get_file_contents(filename: str) -> list[str]:
    with open(filename) as f:
        out = f.readlines()
        return [x.strip() for x in out]
