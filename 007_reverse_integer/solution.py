import math

def reverse(x):
    myMax = 2147483647

    if x == 0: return 0
    isPos = x/math.fabs(x)
    x = math.fabs(x)
    solution = 0
    while (x > 0):
        if math.fabs(solution) > myMax // 10:
            return 0
        solution *= 10
        solution += x%10
        x = x//10


    

    return int(solution * isPos)

print(reverse(321))#123
print(reverse(0)) #0
print(reverse(-123)) #-321
print(reverse(4)) #4
print(reverse(2147483647)) #0 b/c overflow
print(reverse(-2147483647)) #0 b/c overflow
