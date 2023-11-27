def count_reversed_coins(
        array: list,
):
    flips = 0
    if len(array) > 1 and array[1] == array[0]:
        flips += 1
        array[1] = 0 if array[0] == 1 else 1
    for i in range(len(array) - 2):
        if array[i + 2] != array[i % 2]:
            flips += 1
    return flips


print(count_reversed_coins([1, 0, 1, 0, 1, 1]))
print(count_reversed_coins([1, 1, 0, 1, 1]))
print(count_reversed_coins([0, 1, 0]))
print(count_reversed_coins([0, 1, 1, 0]))
print(count_reversed_coins([0]))
print(count_reversed_coins([1, 1, 1, 1, 1]))
