# vowels = ["a","e","i","o","u"]
# string = "hello there fellow manperson"
# new_arr = []
# i = 0
# while i < len(string):
#     if string[i] not in vowels:
#         new_arr.append(string[i])
#     i += 1
#
# print(sorted(set(new_arr)))

vowels = frozenset("aeiou")
sampleText = "Python is a very powerful language"

finalSet = set(sampleText).difference(vowels)
print(sorted(finalSet))