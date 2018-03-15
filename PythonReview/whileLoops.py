# for i in range(0,10):
#     print("i is now {}".format(i))
#
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1
#
# available_exits = ["east","north east", "south"]
#
# chosen_exit = ""
#
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
#
# print("aren't you glad you got out of there")

# import random
# highest = 10
# answer = random.randint(1, highest)
#
# print("Please guess a number between 1 and {}:".format(highest))
# guess = int(input())
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print("Sorry wrong guess")
# else:
#     print("You got it first time!")

import random
highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}:".format(highest))
guess = int(input())
while guess != answer:
    if guess < answer:
        print("Number is higher")
    if guess > answer:
        print("Number is lower")
    guess = int(input())
else:
    print("You guess it! Great job!")