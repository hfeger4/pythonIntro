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

# Inefficient
# def rec_coin(target, coins):
#
#     min_coins = target
#
#     if target in coins:
#         return 1
#     else:

#for every coin value that is <= my target

#         for i in [c for c in coins if c <= target]:
# add coin count and start recursive call
#             num_coins = 1 + rec_coin(target-i,coins)
#  Reset minimum if the new num_coins is less than min_coins
#             if num_coins < min_coins:
#                 min_coins = num_coins
#     return min_coins

def rec_coin_dynam(target, coins, known_results):
    min_coins = target

    if target in coins:
        known_results[target] = 1
        return 1
    #return known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    else:
        #for every coin value <= target,
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin_dynam(target-i, coins, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                #reset known result
                known_results[target] = min_coins
    return min_coins

print(rec_coin_dynam(63,[1,5,10,25],[0]*(63+1)))
