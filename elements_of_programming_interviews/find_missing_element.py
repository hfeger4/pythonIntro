
# My solution:
# def finder(arr1,arr2):
#     arr2.sort()
#     arr1.sort()
#     for i in range(len(arr1)-1):
#         if arr1[i] != arr2[i]:
#             missing = arr1[i]
#             break
#     return ("{} is the missing number".format(missing))

# His solution 1
# def finder(arr1, arr2):
#     arr1.sort()
#     arr2.sort()
#
#     for num1,num2 in zip(num1,num2):
#         if num1 != num2:
#             return num1
#     return arr1[-1]

# Interview solution

import collections


def finder(arr1,arr2):
    hash = collections.defaultdict(int)

    for num in arr2:
        hash[num] += 1
    for num in arr1:
        if hash[num] == 0:
            return num
        else:
            hash[num] -= 1

print(finder([1,2,3,4],[1,3,4]))


