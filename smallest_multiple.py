# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Euler #5

def smallest_multiple(n):
    arr = []
    for i in range(n + 1):
        if is_prime(i):
            arr.append(i)
    return exponent(arr, n)

def is_prime(n):
    if n >= 2:
        for i in range(2, n):
            if not (n % i):
                return False
    else:
        return False
    return True

def exponent(arr, n):
    exp = 1
    for i in arr:
        for x in range(1, n + 1):
            if i**x > n:
                exp *= i**(x - 1)
                break
    return exp

print(smallest_multiple(20))