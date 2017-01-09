def count_primes(n):
    if n <= 1:
        return 0
    numbersLessThanN = [True for i in range(0,n)]
    numbersLessThanN[0] = False
    numbersLessThanN[1] = False
    for i in range(n):
        if numbersLessThanN[i]:
            j = i * 2
            while (j < n):
                numbersLessThanN[j] = False
                j += i
    return sum(numbersLessThanN)


print(count_primes(1)) #0
print(count_primes(6)) #3
print(count_primes(0)) #0
print(count_primes(2)) #0
