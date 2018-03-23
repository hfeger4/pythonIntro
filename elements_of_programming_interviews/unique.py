def uni_char(s):
    return len(s) == len(set(s))

# def uni_char(s):
#     hash = {}
#     for letter in s:
#         if letter in hash:
#             hash[letter] += 1
#         else:
#             hash[letter] = 1
#
#     for count in hash:
#         if hash[count] > 1:
#             return False
#
#     return True

# def uni_char(s):
#     my_set = set()
#
#     for char in s:
#         if char in my_set:
#             return False
#         else:
#             my_set.add(char)
#     return True

print(uni_char('abcdefg') == True)
print(uni_char('abcdefgg') == False)
print(uni_char('abcedefg') == False)