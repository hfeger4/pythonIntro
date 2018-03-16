farm_animals = {"sheep","cow","hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

wild_animals = set(["lion","tiger","panther"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("rooster")
wild_animals.add("Dzung")

print(farm_animals)
print(wild_animals)

empty_set = set()
empty_set2 = {}
empty_set.add("hello")
print(empty_set)
# empty_set2.add("no") Cant add if you initiate a set as empty open brackets, needs a value
print(empty_set2)

even = set(range(0,40,2))
print(even)
squares_tuple = (4,6,9,16,25)
squares = set(squares_tuple)
print(squares)
even = set(range(0,40,2))
print(even)
print(len(even))

print(even.union(squares))
print(len(even.union(squares)))

print(squares.union(even))

print("-" * 40)

print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)

print(sorted(even))

#subtracting B from A removing items from B that are in A
print("even")
print(even)
print("squares")
print(squares)
print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(sorted(squares - even))

# print("-" * 40)
# print(even)
# even.difference_update(squares)
# print(even)

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))
print(sorted(squares.symmetric_difference(even)))


# squares.discard(4)
# squares.remove(16) #remove throws an error if this number doesnt exist.
# squares.discard(8)
# print(squares)

# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not in the set")
print("Subsets")
even = set(range(0,40,2))
print(even)
squares_tuple = (4,6,16)
squares = set(squares_tuple)
print(squares)

if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a superset of squares")

even = frozenset(range(0,100,2))