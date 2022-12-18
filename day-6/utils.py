def load_input_file(filename: str) -> str:
    with open(filename) as f:
        out = f.read()
        return out.strip()


def get_unique_chars(input_string: str, length: int) -> str:
    marker = 0
    for i in range(0, len(input_string) - length - 1):
        chars = set(input_string[i:i + length])
        if len(chars) == length:
            marker = i + length
            break
    return input_string[marker:marker + length]
