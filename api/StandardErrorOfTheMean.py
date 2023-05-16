import math

varianceEstimate = 1.25         # variance(sigma hat), NOT SQUARED
sampleSize = 121               # n
populationSize = 1700           # N

# uncomment and fill in if you need variance using points
# xList = []
# xBar = getMean(xList)

def getSE(sigma, n):
    return  sigma / math.sqrt(n) 

def geSEWithFPC(sigma, littleN, bigN):
    return (sigma / math.sqrt(littleN)) * (math.sqrt((bigN - littleN) / (bigN - 1)))

def getVarianceSquared(xList, xBar):
    variance = 0
    for i in xList:
        variance += math.pow((xList[i] - xBar), 2)

    return variance / 2

def getXBar(xList):
    xBar = 0
    for i in xList:
        xBar = xBar + i

    return round(xBar / len(xList), 2)

# print("SE:\t\t" + (str)(getSE(varianceEstimate, sampleSize)))
# # print("SE(FPC):\t" + (str)(geSEWithFPC(varianceEstimate, sampleSize, populationSize)))

# # uncomment if you need variance using points
# print("SE(FPC):\t" + (str)(getVarianceSquared(xList, xBar)))