"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


import collections

def missing_positive(array):

    max_num = max(array)
    hash_int = collections.defaultdict(int)

    for num in array:
        hash_int[num] += 1

    for i in range(max_num):
        if hash_int[i] == 0 and i != 0:
            return i
    return max_num + 1


print(missing_positive([1, 2, 0]))
print(missing_positive([3, 4, -1, 1]))
print(missing_positive([0, 2, 1, 2, 2, 3, 4, 6, 7, 8, 9, 10, -1, -2, -10]))
