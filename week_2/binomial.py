import math

def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n

def combination(i, N):
    return factorial(N)/(factorial(i)*factorial(N - i))

def prob(n, p, N):
    return combination(n, N) * (p ** n) * (1 - p)**(N - n)

def infoMeasure(n, p, N):
    return -math.log(prob(n, p, N), 2)

def sumProb(N, p):
    sum = 0 
    for i in range(1, N + 1):
        sum += prob(i, p, N)

    return sum

def approxEntropy(N, p):
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p, N) * infoMeasure(i, p, N)
        
    return sum

print(approxEntropy(3, 0.5))

