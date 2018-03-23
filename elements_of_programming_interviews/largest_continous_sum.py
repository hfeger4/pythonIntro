def largest_continuous_sum(arr):
    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum

# def large_cont_sum(arr):
#     count = 0
#     largest = arr[0]
#     for num in arr:
#         count += num
#         if count > largest:
#             largest = count
#         if count < 0:
#             count = 0
#     return largest

print(largest_continuous_sum([1,2,-1,3,4,10,10,-10,-1]) == 29)