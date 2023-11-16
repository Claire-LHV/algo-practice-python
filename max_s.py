"""
Task description
You are given an aray Aof Nintegers. You can delete some (possibly zero) of its elements. Then the remaining elements ni even positions are added and elements in odd positions are subtracted:
S=A[0] - A[1] +A[2] - A[3] +
What is the maximum possible value of S that could be obtained by performing such deletions? As the result may be large, return its last nine digits without leading zeros (in other words, return the result modulo 1,000,000,000).
Write a function:
class Solution { public int solution(int[] A); }
that, gvien na aray Aof length , returns the maxmi um value of S(modulo 1,000,000,000).
Examples:
1. Given A= 14, 1, 2, 3], the function should return 6, because we could delete the third value in A and obtain A= 14, 1, 3]. Then S = 4 - 1 + 3= 6, which is the maximum possible value of S.
2. Given A= [1, 2, 3, 3, 2, ,1 5], the function should return 7, because for A= [3, 1, 5] we could obtain =S 3 - 1 + 5 = 7.
3. Given A=[1000000000, 1, 2, 2, 1000000000, 1, 1000000000], the function should return 999999998, because for A=[1000000000, 1, 1000000000, 1, 1000000000] we could obtain S = 1000000000 - 1 + 1000000000 - 1 - 1000000000 = 2999999998. That is the
maximum possible value of S, but it should be returned modulo 1000000000. Write an efficient algorithm for the following assumptions:
• N is an integer within the range [1..200,000];
• each element of array Ais an integer within the range [... 1,000,000,000).
"""


def get_max_s(
        array,
) -> int:
    """
    The idea is to get first local max to be in the first even position A[0],
    then next is the following local min to be in the odd position A[1],
    and continue until the end, and always stop at the last high.
    :param array:
    :return:
    """
    array.append(0)
    new_array = []
    result = 0
    next_high = array[0]
    next_low = array[0]
    for i in array:
        print('i', i)
        print('current next_high', next_high)
        print('current next_low', next_low)
        if len(new_array) % 2 == 0:
            print('looking for next_high')
            if i >= next_high:
                next_high = i
                print('set new next_high', next_high)
            else:
                new_array.append(next_high)
                result += next_high
                print('Found and saved next_high!', new_array)
                next_low = i
                print('set next new next_low', next_low)
        else:
            print('looking for next_low')
            if i <= next_low:
                next_low = i
                print('set new next_low', next_low)
            else:
                new_array.append(next_low)
                result -= next_low
                print('Found and saved next_low!', new_array)
                next_high = i
                print('set next new next_high', next_high)
        print('----------------------------')
    print('final new array ', new_array)
    print('result', result % 1000000000)
    return result % 1000000000


AS = [
    [4, 1, 2, 3],
    [1, 2, 3, 3, 2, 1, 5],
    [1000000000, 1, 2, 2, 3, 4, 34634, 1000000000, 1, 2346534, 2345, 23523,
     1000000000, 1, 1000000000],
]


def get_max_s_refactored(
        array,
) -> int:
    """
    The idea is to get first local max to be in the first even position A[0],
    then next is the following local min to be in the odd position A[1],
    and continue until the end, and always stop at the last high.
    :param array: array of integers
    :return: int max_total % 1000000000
    """
    array.append(0)
    new_array = []
    result = 0
    previous = array[0]
    for i in array:
        if len(new_array) % 2 == 0:
            if i >= previous:
                previous = i
            else:
                new_array.append(previous)
                result += previous
                previous = i
        else:
            if i <= previous:
                previous = i
            else:
                new_array.append(previous)
                result -= previous
                previous = i
    print('final new array ', new_array)
    print('result', result % 1000000000)
    return result % 1000000000


for A in AS:
    get_max_s_refactored(A)
