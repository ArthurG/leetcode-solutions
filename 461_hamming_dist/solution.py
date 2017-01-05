def hammingDistance(x, y):
    counter = 0
    while (x > 0 or y > 0):
        if (x % 2 != y % 2):
            counter+=1
        x = x// 2
        y = y//2
    return counter

print(hammingDistance(1, 4)) #2
print(hammingDistance(4, 4)) #0
print(hammingDistance(7, 8)) #4
print(hammingDistance(9, 8)) #1
print(hammingDistance(0, 8)) #1
print(hammingDistance(8, 0)) #1
