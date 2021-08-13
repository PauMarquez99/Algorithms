def parenthesis():
    inTry = input("Input to check:")
    stack = []
    for letter in inTry:
        if (letter == '(' or letter == '['):
            stack.append(letter)
        else:
            if len(stack)==0:
                return False
            else:
                compare = stack.pop()
                if letter == ')' and compare != '(':
                    return False
                elif letter == ']' and compare != '[':
                    return False
    if len(stack) != 0:
        return False
    return True

print(parenthesis())
