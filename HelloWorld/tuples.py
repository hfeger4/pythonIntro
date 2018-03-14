t = "a","b","c"
print(t)

print("a","b","c")
print(("a","b","c"))


types = "Lightning","Snow",100

print(types)
print(types[0])
print(types[2])

# types[0] = "Fire"
# tuples are immutable, but you can do this instead!

types = "Fire", types[1], types[2]
print(types)

#Unpacking the tuple.

pokemon = "Pikachu","Raichu",100

first_form, second_form, attack = pokemon

print(first_form)
print(second_form)
print(attack)

# pokemon.append("Hello")
# cannot append tuples.

poke_info = "Pikachu","Raichu",100,(
    ("weaknesses",2),("strengths",5),("kills",100000))


first, second, attack_level, info = poke_info
print(first)
print(second)
print(attack_level)
print(info)

for details in info:
    main,detail = details
    print("\tMain info: {} Detail info: {}".format(main,detail))
