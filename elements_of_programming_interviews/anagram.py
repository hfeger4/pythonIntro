def anagram(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    hash = {}

    for letter in s1:
        if letter in hash:
            hash[letter] += 1
        else:
            hash[letter] = 1

    for letter in s2:
        if letter in hash:
            hash[letter] -= 1
        else:
            hash[letter] = 1

    for count in hash:
        if hash[count] != 0:
            return False

    return True

print(anagram("god", "dog") == True)
print(anagram("go od", "d OO g") == True)
print(anagram("oh","ooh") == False)