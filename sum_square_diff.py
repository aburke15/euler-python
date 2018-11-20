# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# Euler 6

def square_then_sum(n):
    return (n * (n + 1) * ((2 * n) + 1)) / 6

def sum_then_square(n):
    return ((n * (n + 1)) / 2)**2

n = 100
result = sum_then_square(n) - square_then_sum(n)
print(result)