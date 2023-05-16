import math

list = [2, 2, 1, 3, 3, 0, 1, 3, 0, 3, 6, 1, 2]

def getMean(list):
    mean = 0
    for i in list:
        mean = mean + i
    mean = mean / len(list)

    return mean

def getRange(list):
    return max(list) - min(list)

def getStandardDeviation(list, mean):
    nominator = 0
    for i in list:
        nominator += math.pow((i - mean), 2)

    nominator = (nominator / len(list))
    return math.sqrt(nominator)

mean = getMean(list)

print("----------Info on Data----------")
print("Std.Dev.: " + (str)(getStandardDeviation(list, mean)))
print("Mean: "+ (str)(mean))
print("Range: " + (str)(getRange(list)))