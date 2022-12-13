import json


def read_input_from_file(filename):
    with open(filename, 'r') as f:
        out = f.readlines()
        # skip empty lines
        out = [x.strip() for x in out if x.strip()]
    return out


def split_into_pairs(inp) -> list[list]:
    out = []
    for i in range(0, len(inp), 2):
        out.append(inp[i:i + 2])
    return out


def parse_multidimensional_array(string: str) -> list[any]:
    """Parse a multidimensional array from a string.
    Example:
        string: '[[1,2],[3,4]]'
        output: [[1,2],[3,4]]
    """
    return json.loads(string)