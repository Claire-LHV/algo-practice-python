def find_max_profit(
        array: list,
):
    if len(array) == 0:
        return 0
    buy_in = array[0]
    max_profit = 0

    for val in array:
        if val < buy_in:
            buy_in = val
        elif val - buy_in > max_profit:
            max_profit = val - buy_in
    return max_profit


print(find_max_profit([23171, 21011, 21123, 21366, 21013, 21367]))
print(find_max_profit([1, 2, 3, 4, 5]))
print(find_max_profit([7, 6, 4, 3, 1]))
print(find_max_profit([]))
print(find_max_profit([1, 2, 3, 4, 10, 6, 7, 8, 9, 5]))
