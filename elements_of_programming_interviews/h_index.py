"""
Given an array of positive inetegers, find the largest h such that there are at least h
entries in the array that are greater than or equal to h
"""


def h_index(array):
    array.sort()
    length = len(array)
    i = 0
    while i < length:
        if array[i] >= length - i:
            return length - i
        i += 1

    return 0




print(h_index([1, 4, 1, 4, 2, 1, 3, 5, 6]))


#Answer----
# def h_index(array):
#     array.sort()
#     length = len(array)
#     for i, c in enumerate(array):
#         if c >= length - i:
#             return length - i
#     return 0