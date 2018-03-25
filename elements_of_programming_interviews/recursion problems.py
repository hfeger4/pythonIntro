def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n-1)

print(recursive_sum(10))

def sum_split(n):
    if n < 10:
        return n
    else:
        return n % 10 + (sum_split(n//10))

print(sum_split(4321))

def word_split(phrase, list_of_words, output = None):
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)
    return output




print(word_split('themanran',['the','ran','man']))
print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
print(word_split('themanran',['clown','ran','man']))

def reverse_string(str):
    if len(str) == 1:
        return str
    else:
        return str[-1] + reverse_string(str[:-1])

print(reverse_string("hello"))


