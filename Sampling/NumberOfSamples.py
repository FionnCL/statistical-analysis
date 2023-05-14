import math

littleN = 2
bigN = 3
list = [1, 2, 3]

def ssOrderedNoRep(n, N):
    return math.factorial(N) / math.factorial(N - n)

def ssUnorderedNoRep(n, N):
    return math.factorial(N) / (math.factorial(n) * math.factorial(N - n))

def ssOrderedRep(n, N):
    return math.pow(N, n)

def ssUnorderedRep(n, N):
    return math.factorial(N + n - 1) / (math.factorial(n) * math.factorial(N - 1))

def isIndependent(list):
    i = 0
    while(i < len(list)):
        j = i + 1
        while(j < len(list)):
            if list[i] == list [j]:
                return False
            j += 1
        i += 1
    return True

print("--------No Repetition--------")
print("Ordered SS:\t" + (str)(ssOrderedNoRep(littleN, bigN)))
print("Unordered SS:\t" + (str)(ssUnorderedNoRep(littleN, bigN)))
print("----------Repetition----------")
print("Ordered SS:\t" + (str)(ssOrderedRep(littleN, bigN)))
print("Unordered SS:\t" + (str)(ssUnorderedRep(littleN, bigN)))
print("---------Independence---------")
print("Independent(WRONG):\t" + (str)(isIndependent(list)))