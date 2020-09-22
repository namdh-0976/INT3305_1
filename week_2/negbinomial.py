import math

def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n

def combination(i, N):
    return factorial(N) / (factorial(i) * factorial(N - i))

def prob(n, p, r):
    return combination(n - r + 1, n) * (p**n) * (1 - p) ** r

def infoMeasure(n, p, r):
    return -math.log(prob(n, p, r), 2)

def sumProb(N, p, r):
    sum = 0 
    for i in range(1, N + 1):
        sum += prob(i, p, r)

    return sum

def approxEntropy(N, p, r):
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p, r) * infoMeasure(i, p, r)

    return sum

print(approxEntropy(5, 0.5, 2))

