def countAndSay(n):
    currNumString = "1"
    for i in range(n - 1 ):
        m = []
        m.append([currNumString[0], 0])
        for char in currNumString:
            if m[-1][0] == char:
                m[-1][1] += 1
            else:
                m.append([char, 1])

        currNumString = ''.join([''.join([str(innerElem) for innerElem in elem[::-1]]) for elem in m])
    return currNumString

print(countAndSay(1)) #1
print(countAndSay(0)) #0
print(countAndSay(2)) #11
print(countAndSay(3)) #21

