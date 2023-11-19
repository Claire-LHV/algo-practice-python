def get_sum_of_digits(
        n: int,
):
    sum_of_digits = 0
    num = n
    while int(num / 10) != 0:
        sum_of_digits += num % 10
        num = int(num / 10)
    return sum_of_digits + num % 10


def get_max_pair_sum(
        array: list,
):
    if len(array) < 2:
        return 0  # we don't want to include this

    greatest = second_greatest = 0
    for val in array:
        if val >= greatest:
            second_greatest = greatest
            greatest = val
        elif val > second_greatest:
            second_greatest = val
    return second_greatest + greatest


def solution(
        array: list,
):
    sum_digits_indexes = {}
    for index, num in enumerate(array):
        sum_digits_indexes.update(
            {
                get_sum_of_digits(num): sum_digits_indexes.get(
                    get_sum_of_digits(num), []) + [num]
            }
        )
    max_sum = 0
    for sub_array in sum_digits_indexes.values():
        this_sum = get_max_pair_sum(sub_array)
        if this_sum > max_sum:
            max_sum = this_sum
    return max_sum if max_sum else -1


print(solution([123, 321, 456, 654, 789, 321, 4, 9, 63, 231, 213, 312, 534, 4233]))
print(solution([51, 71, 17, 42]))
print(solution([43, 33, 60]))
print(solution([51, 32, 43]))
