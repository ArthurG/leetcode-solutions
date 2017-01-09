def add_digits(num):
    if not num:
        return num
    return num - 9  * ((num - 1 ) // 9)



print(add_digits(38)) #2
print(add_digits(65536)) #7
print(add_digits(0)) #0
print(add_digits(9)) #9
