string = "1234567890"

# for char in string:
#     print(char)

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# # print(next(my_iterator)) Will be an error
#
# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)

nums = [1,2,3,4,5,6,7,8]
my_nums = iter(nums)

for i in range(0,len(nums)):
    next_item = next(my_nums)
    print(next_item)