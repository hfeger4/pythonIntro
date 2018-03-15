#unordered key value pairs

fruit = {"orange":"a sweet, orange, citrus fruit",
         "apple":"good for making cider",
         "banana": "good for measuring stuff",
         "lime" : "a sour thing"
         }

print(fruit)
print(fruit["apple"])

bike = {
    "make" : "honda",
    "model" : "focus",
    "color" : "red",
    "engine_size" : 250,
    "make" : "not honda" #shows the last key entered matters, duplicates are ok but give warnings
}

print(bike["engine_size"])

bike["wheels"] = True

print(bike["wheels"])

print(bike)

del bike["wheels"]
print(bike)
#del bike           deletes bike entirely.
bike.clear()
print(bike)

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == 'quit':
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key) #doesnt throw error if unit doesnt exist
#     # description = fruit[dict_key]
#     print(description)
#     #if dict_key in fruit: To check if the key is in fruit.
#     #fruit.has_key(dict_key) Is a python 2 method, deprecated.
#
# for snack in fruit:
#     print(fruit[snack])
#

# for i in range(1):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])

# ordered_keys = sorted(list(fruit.keys()))
# # ordered_keys.sort()
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])
#
# for val in fruit.values():
#     print(val)

# print(fruit.keys())
# print(fruit.values())

print(fruit)
print(fruit.items)

#Turn into tuples
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

#Turn back into dictionary
print(dict(f_tuple))