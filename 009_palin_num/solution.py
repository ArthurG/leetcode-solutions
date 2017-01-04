import math

def isPalindrome(x):
    if x < 0:
        return False
    if (x < 10):
        return True
    numDigits = int(math.log10(x)) + 1
    for i in range(int(numDigits // 2)):
        firstDigit = (x // math.pow(10, numDigits - i - 1)) % 10
        lastDigit = (x // math.pow(10, i)) % 10
        if (firstDigit != lastDigit):
            return False
    return True



print(isPalindrome(1)) #T
print(isPalindrome(0)) #T
print(isPalindrome(11)) #T
print(isPalindrome(-11)) #F
print(isPalindrome(15)) #F
print(isPalindrome(100)) #F
print(isPalindrome(101)) #T
print(isPalindrome(13531)) #T
