def isValid(s):
    stk = []
    for i in range(len(s)):
        if (s[i] == "(" or s[i] == "{" or s[i] == "["):
            stk.append(s[i])
        elif len(stk) == 0:
            return False
        elif (s[i] == ")" and stk[-1] == "("):
            stk.pop()
        elif (s[i] == "}" and stk[-1] == "{"):
            stk.pop()
        elif (s[i] == "]" and stk[-1] == "["):
            stk.pop()
        else:
            return False
    if(len(stk) == 0):
        return True
    else:
        return False


print(isValid("")) #true
print(isValid("()[]{}")) #true
print(isValid("([]{})")) #true
print(isValid("(")) #false
print(isValid(")")) #false
print(isValid("([)]")) #false
