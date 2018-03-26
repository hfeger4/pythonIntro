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


def permute(s):
    out = []
    if len(s) == 1:
        out = [s]

    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i + 1:]):
                out += [let + perm]

    return out

print(permute('abc'))

def fib_recursive(num):
    if num == 0 or num == 1:
        return num
    return fib_recursive(num-1) + fib_recursive(num-2)

print(fib_recursive(10))

n = 12
cache = [None] * (n + 1)

def fib_dynamic(n):
    if n == 0 or n == 1:
        return n
    if cache[n] != None:
        return cache[n]
    cache[n] = fib_dynamic(n-1) + fib_dynamic(n-2)

    return cache[n]

def fib_iterative_his_version(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a+b

    return a


def fib_iterative(n):
    arr = [0,1]
    position  = 2
    if n == 0 or n == 1:
        return n

    while position <= n:
        arr.append(arr[-2] + arr[-1])
        position += 1

    return arr[-1]

print(fib_iterative(10))




