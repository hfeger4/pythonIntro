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


for char in number:
    if char in '0123456789':
        cleanedNumber += char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin'", "no more","a stiff", "bereft of lift"]:
    print("This parrot is " + state)
    #print("This parrot is {}".format(state))

for i in range(0,100,5):
    print("i is {}".format(i))

for i in range(1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i, j ,i*j), end="\t")
    # print("================================")
    print(" ")
