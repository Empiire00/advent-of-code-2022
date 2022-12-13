import utils


def compare_arrays(arr1, arr2) -> int:
    """Compare arrays arr1 to arr2
        return -1 if arr1 is smaller than arr2
        return 1 if arr1 is bigger than arr2
        return 0 if arr1 is equal to arr2
    """
    if type(arr1) == int and type(arr2) == int:
        if arr1 < arr2:
            return -1
        elif arr1 > arr2:
            return 1
        else:
            return 0
    elif type(arr1) == list and type(arr2) == int:
        arr2 = [arr2]
        return compare_arrays(arr1, arr2)
    elif type(arr1) == int and type(arr2) == list:
        arr1 = [arr1]
        return compare_arrays(arr1, arr2)
    # if arr1 runs out of elements, it is sorted
    elif not arr1 and arr2:
        return -1
    # if arr2 runs out of elements, it is not sorted
    elif arr1 and not arr2:
        return 1
    elif not arr1 and not arr2:
        return 0
    else:
        # compare first elements
        first = compare_arrays(arr1[0], arr2[0])
        if first == 0:
            # if first elements are equal, compare the rest
            return compare_arrays(arr1[1:], arr2[1:])
        else:
            return first


def main():
    inp = utils.read_input_from_file('input.txt')
    parsed_input = list(map(utils.parse_multidimensional_array, inp))
    pairs = utils.split_into_pairs(parsed_input)

    # I really like python :D
    sum_of_sorted = sum([index + 1 for (index), pair in enumerate(pairs) if compare_arrays(pair[0], pair[1]) == -1])
    print(sum_of_sorted)


if __name__ == "__main__":
    main()
