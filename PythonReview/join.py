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

vocabulary = { "QUIT" : "Q",
               "NORTH" : "N",
               "SOUTH" : "S",
               "EAST" : "E",
               "WEST": "W"}

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

# hello = "hello, there".split()
# print(hello)