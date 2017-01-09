def canWinNim(n):
    return not (n % 4 == 0)

print(canWinNim(1)) #t
print(canWinNim(2)) #t
print(canWinNim(3)) #T
print(canWinNim(4)) #f
print(canWinNim(5)) #t
print(canWinNim(6)) #t
print(canWinNim(7)) #t
print(canWinNim(8)) #f
print(canWinNim(9)) #t
