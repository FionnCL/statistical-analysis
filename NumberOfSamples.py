import math

def orderedNoRep(n, N):
    return math.factorial(N) / math.factorial(N - n)

def unorderedNoRep(n, N):
    return math.factorial(N) / (math.factorial(n) * math.factorial(N - n))

def orderedRep(n, N):
    return math.pow(N, n)

def unorderedRep(n, N):
    return math.factorial(N + n - 1) / (math.factorial(n) * math.factorial(N - 1))