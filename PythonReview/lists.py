# ipAddress = input("Please enter an IP address")
# print(ipAddress.count("."))


# game_list = ["halo","CS","GunBlade"]
# game_list.append("Witcher")
# for game in game_list:
#     print("An awesome game is {}".format(game))
#
#
# even = [2,4,6]
# odd = [1,3,5]
#
# numbers = odd + even
# # numbers.sort()
# sorted_numbers = sorted(numbers)
# print(numbers)
#
# if numbers == sorted_numbers:
#     print("The lists are equal")
# else:
#     print("The lists arent equal")
#
#
# list1 = []
# list2 = list()
#
# print(list("Hello world"))

# even = [2,4,6,8]
#
# another_even = list(even)
# another_even.sort(reverse=True)
# print(even)
# print(another_even)

menu = []
menu.append(["egg","spam","bacon"])
menu.append(["egg","spam","bacon"])
menu.append(["egg","spam","bacon"])
menu.append(["egg","spam","bacon"])
menu.append(["egg","spam","bacon"])
menu.append(["egg","bacon"])
print(menu)

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)

