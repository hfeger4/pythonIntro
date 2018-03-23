# def rev_word(s):
#     return " ".join(reversed(s.split()))
#

def rev_word(s):
    words = []
    i = 0
    while i < len(s):
        if s[i] != " ":
            word_start = i

            while i < len(s) and s[i] != " ":
                i += 1
            words.append(s[word_start:i])
        i += 1
    i = 0
    while i < len(words)//2:
        words[i], words[~i] = words[~i], words[i]
        i += 1
    return " ".join(words)


print(rev_word("Well    no  you cant   "))