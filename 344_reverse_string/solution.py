def reverseString(s):
    newS = []
    for i in range(len(s)-1,-1,-1):
        newS.append(s[i])
    return ''.join(newS)

print(reverseString("hello")) #olleh
print(reverseString("i Am ")) # mA i


