fruit = {"orange":"a sweet, orange, citrus fruit",
         "apple":"good for making cider",
         "banana": "good for measuring stuff",
         "lime" : "a sour thing"
         }

print(fruit)

veg = {"cabbage" : "good with beans",
       "tomatoe" : "good with pasta",
       "grass" : "good for cows"
}

print(veg)
#
# veg.update(fruit)
# print(veg)
#
# print(fruit.update(veg))
# print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
print(fruit)
print(veg)

myList = ["a","b","c","d"]
letters = "abcdefghijklmnopqrstuvwxyz"

newString = ", ".join(myList)
alpha = " ".join(letters)

print(newString)
print(alpha)

locations = {0: "You are sitting in front of a computer learning python",
             1: "You are standing in front of a brick building",
             2: "You are on top of a hill",
             3: "You are inside a building",
             4: "You are in a valley",
             5: "You are in a forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q":0},
         2: {"N":5, "Q":0},
         3: {"W":1, "Q":0},
         4: {"N":1,"W":2, "Q":0 },
         5: {"W":2, "S":1, "Q":0}
         }

named_exits = {1: {"2" : 2} }

vocabulary = { "QUIT" : "Q",
               "NORTH" : "N",
               "SOUTH" : "S",
               "EAST" : "E",
               "WEST": "W",
               "ROAD": "1",
               "Hill": "2",
               "Valley" : "4",
               "Building": "3",
               "Forest" : "5"}

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break
    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    #parse the user input
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary.keys():
                direction = vocabulary[word]
                break
        # for word in vocabulary.keys():
        #     if word in direction:
        #         direction = vocabulary[word]
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")



