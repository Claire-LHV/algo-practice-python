def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_prime_numbers_in_range(a: int, b: int):
    count = 0
    if a == 2:
        count += 1
    start = a + 1 if a % 2 == 0 else a
    for i in range(start, b + 1, 2):
        if is_prime(i):
            count += 1
    return count


print(count_prime_numbers_in_range(2, 10))
print(count_prime_numbers_in_range(3, 15))
print(count_prime_numbers_in_range(10, 50))
print(count_prime_numbers_in_range(100, 200))
