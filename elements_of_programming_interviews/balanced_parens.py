def balanced_parens(arr):
    stack = []
    open_parens = ["[","{","("]

    for paren in arr:
        if paren in open_parens:
            stack.append(paren)
        else:
            if stack == [] or not matching(stack.pop(),paren):
                return False

    return stack == []



def matching(opener, closer):
    if opener == "[" and closer == "]":
        return True
    if opener == "(" and closer == ")":
        return True
    if opener == "{" and closer == "}":
        return True

print(balanced_parens("([)]") == False)
print(balanced_parens("[()]"))
print(balanced_parens("[]"))

