import math

# SIMPLY INPUT THE X and Y values and everything will be given to you.

# xList = [0.56, 0.23, 1.56, 0.07, 0.13, 1.72, 0.46, 1.27, 0.69, 0.45, 1.22, 0.36, 0.40, 0.11, 0.56]
# yList = [2.18, -0.66, 0.21, -2.51, -2.63, 1.27, -0.17, 0.78, 0.02, -0.63, 0.07, 0.46, -0.04, -3.57, 1.63]

def getBeta(xList, yList, xBar, yBar):
    numerator = 0
    denominator = 0
    for i in range(len(xList)):
        numerator += ((xList[i] - xBar) * (yList[i] - yBar))
        denominator += math.pow((xList[i] - xBar), 2)

    return numerator / denominator

# returns tuple
def getMeans(xList, yList):
    xBar = 0
    yBar = 0
    for i in xList:
        xBar = xBar + i
    xBar = round(xBar / len(xList), 2)

    for i in yList:
        yBar = yBar + i

    yBar = round(yBar / len(yList), 2)

    return(xBar, yBar)

def getAlpha(xBar, yBar, beta):
    return yBar - (xBar * beta)



def getPopulationCovariance(xList, yList, xBar, yBar):
    numerator = 0
    for i in range(len(xList)):
        numerator += (xList[i] - xBar) * (yList[i] - yBar)

    return numerator / (len(xList))

def getSampleCovariance(xList, yList, xBar, yBar):
    numerator = 0
    for i in range(len(xList)):
        numerator += (xList[i] - xBar) * (yList[i] - yBar)

    return numerator / (len(xList) - 1)

def getPopulationVariance(list, mean):
    variance = 0
    for i in range(len(list)):
        variance += math.pow((list[i] - mean), 2)

    return variance / len(list)

def getSampleVariance(list, mean):
    variance = 0
    for i in range(len(list)):
        variance += math.pow((list[i] - mean), 2)

    return variance / (len(list) - 1)

# NOTE: Stopped dividing by n.
def getCorrelation(xList, yList, xBar, yBar):
    numerator = 0
    denominator1 = 0
    denominator2 = 0
    for i in range(len(xList)):
        numerator += (xList[i] - xBar) * (yList[i] - yBar)

    for i in range(len(xList)):
        denominator1 += math.pow((xList[i] - xBar), 2)
    denominator1 = math.sqrt(denominator1)

    for i in range(len(yList)):
        denominator2 += math.pow((yList[i] - yBar), 2)
    denominator2 = math.sqrt(denominator2)

    return numerator / (denominator1 * denominator2)

# bars = getMeans(xList, yList) #returns tuple
# xBar = bars[0]
# yBar = bars[1]
# beta = getBeta(xList, yList, bars[0], bars[1])
# alpha = getAlpha(xBar, yBar, beta)
# populationCovariance = getPopulationCovariance(xList, yList, bars[0], bars[1])
# sampleCovariance = getSampleCovariance(xList, yList, bars[0], bars[1])
# correlation = getCorrelation(xList, yList, bars[0], bars[1])
# popVarX = getPopulationVariance(xList, xBar)
# popVarY = getPopulationVariance(yList, yBar)
# sampleVarX = getSampleVariance(xList, xBar)
# sampleVarY = getSampleVariance(yList, yBar)

# print("--------------------")
# print("X-BAR\t\t=\t\t"+(str)(xBar))
# print("Y-BAR\t\t=\t\t"+(str)(yBar))
# print("ALPHA\t\t=\t\t"+(str)(alpha))
# print("BETA\t\t=\t\t"+(str)(beta))
# print("COR\t\t=\t\t"+(str)(correlation))
# print("--------------------")
# print("POPCOV\t\t=\t\t"+(str)(populationCovariance))
# # print("SAMPCOV\t\t=\t\t"+(str)(sampleCovariance))
# # print("--------------------")
# # print("POPVAR(X)\t=\t\t"+(str)(popVarX))
# # print("POPVAR(Y)\t=\t\t"+(str)(popVarY))
# print("--------------------")
# print("SAMPVAR(X)\t=\t\t"+(str)(sampleVarX))
# print("SAMPVAR(Y)\t=\t\t"+(str)(sampleVarY))
# print("--------------------")