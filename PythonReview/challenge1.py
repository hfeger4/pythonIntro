#Write a small program to ask for a name and an age.
#When both values have been entered, check if the person
#is the right age to go on an 18-30 holiday(they must be
#over 18 and under 31)
#If they are, welcome them to the holiday, otherwise print
#a (polite) message refusing them entry.

name = input("Please enter your name: ")
age = int(input("Please enter your age to continue: "))

if 18 <= age <= 30:
    print("Welcome to your holiday, {0}!".format(name))
elif age < 18:
    print("I'm sorry, you are too young to enjoy this holiday.")
else:
    print("I'm sorry, you are too old to enjoy this holdiay.")