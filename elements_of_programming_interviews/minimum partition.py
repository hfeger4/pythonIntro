"""
Partition a set into two subsets such that the difference of subset sums is minimum
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.

If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Example:

Input:  arr[] = {1, 6, 11, 5}
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12
Subset2 = {11}, sum of Subset2 = 11
"""
#
# def find_min_rec(arr, i, sumCalculated, sumTotal):
#     if i == 0:
#         return abs((sumTotal - sumCalculated) - sumCalculated)
#
#     return min(find_min_rec(arr, i-1, sumCalculated + arr[i-1], sumTotal),
#                find_min_rec(arr, i-1, sumCalculated, sumTotal))
#
# def find_min(arr, n):
#     sumTotal = 0
#     for i in range(len(arr)):
#         sumTotal += arr[i]
#
#     return find_min_rec(arr, n, 0, sumTotal)

