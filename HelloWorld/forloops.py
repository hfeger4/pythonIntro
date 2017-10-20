# for i in range(1,20):
#     print("i is now {}".format(i))
#
# number = "9,233,232,232,563,974"
# for i in range(0, len(number)):
#     print(number[i])

number = "9,233,232,232,563,974"
cleanedNumber = ""
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))


