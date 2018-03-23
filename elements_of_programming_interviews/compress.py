def compress(s):
    length = len(s)
    arr = []

    if length == 0:
        return ""
    if length == 1:
        return "1" + s

    i = 1
    count = 1
    while i < length:
        if s[i] == s[i-1]:
            count += 1
        else:
            arr.append(count)
            arr.append(s[i-1])
            count = 1
        i += 1
    arr.append(count)
    arr.append(s[-1])
    return arr





print(compress('AAAAABBBBCCCC'))
print(compress('c'))