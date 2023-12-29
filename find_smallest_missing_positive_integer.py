def find_smallest_missing_positive_integer(
        array: list
):
    occur = dict()
    max_n = array[0]

    for i in array:
        if i > max_n:
            max_n = i
        if i > 0:
            occur[i] = True

    if max_n <= 0:
        return 1

    for i in range(1, max_n + 1):
        if occur.get(i) is None:
            return i
    return max_n + 1


if __name__ == '__main__':
    AS = [
        [1, 2, 3],
        [-1, -3],
        [1, 3, 6, 4, 1, 2],
        [1, 1, 1, 1, 2, 3, 8, 9, 5, -45, 0, -89]
    ]
    for a in AS:
        print(find_smallest_missing_positive_integer(a))
