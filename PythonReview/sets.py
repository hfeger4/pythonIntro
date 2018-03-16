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