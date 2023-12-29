def get_start_longest_ascending_slice(
        array: list
):
    prev = array[0]
    p = 0
    ps = [0]
    max_len = current_asc_len = 1

    for i in range(1, len(array)):
        if array[i] > prev:
            current_asc_len += 1
        else:
            current_asc_len = 1
            p = i
        if current_asc_len > max_len:
            max_len = current_asc_len
            ps = [p]
        elif current_asc_len == max_len:
            ps.append(p)
        prev = array[i]
    return ps


if __name__ == '__main__':
    arrays = [
        [2, 2, 2, 2, 1, 2, -1, 2, 1, 3],
        [30, 20, 10],
        [2, 2, 2, -1, 1, 2, 200, 0, 1, 3],
        [1],
        [0, 0, 0]
    ]
    for array in arrays:
        print(get_start_longest_ascending_slice(array))
