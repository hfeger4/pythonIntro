number = "1,123,123,321"
cleanedNumber = ""

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

x = 23
x += 1

x -= 4

print(x)
x -= 1
print(x)

greeting = "Good"
greeting += " morning "
print(greeting)

greeting *= 4
print(greeting)