import utils
from functools import cmp_to_key


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
    packets = list(map(utils.parse_multidimensional_array, inp))
    divider_packets = [[[2]], [[6]]]
    # add divider packets
    packets = packets + divider_packets

    sorted_packets = sorted(packets, key=cmp_to_key(compare_arrays))
    divider_indices = [index for index in range(len(sorted_packets)) if sorted_packets[index] in divider_packets]
    decoder_key = 1
    for index in divider_indices:
        decoder_key *= (index + 1)
    print(decoder_key)


if __name__ == "__main__":
    main()
