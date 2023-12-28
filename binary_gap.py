def convert_deci_to_binary(
        number: int,
) -> str:
    binary_number_string = ''
    while number > 0:
        binary_number_string = str(number % 2) + binary_number_string
        number = number // 2
    return binary_number_string


def find_max_binary_gap(
        binary_number_string: str
) -> int:
    start_one = -1
    max_bin_gap = 0
    for i in range(len(binary_number_string)):
        if binary_number_string[i] == '1':
            if start_one == -1:
                start_one = i
            else:
                current_max = i - start_one - 1
                if current_max > max_bin_gap:
                    max_bin_gap = current_max
                start_one = i
    return max_bin_gap


print(find_max_binary_gap('1001010111101010'))
print(find_max_binary_gap('100000'))
print(find_max_binary_gap('10111111000011'))
