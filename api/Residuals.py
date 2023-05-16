import math

def getEstimatedY(xList, alpha, beta):
    yEstimates = []
    for i in range(len(xList)):
        yEstimates.append(round(alpha + (beta * xList[i]), 4))

    return yEstimates

def getTSS(yList, yBar):
    TSS = 0
    for i in range(len(yList)):
        TSS += math.pow((yList[i] - yBar), 2)
    
    return TSS

def getRSS(yList, yEstimates):
    RSS = 0
    for i in range(len(yList)):
        RSS += math.pow((yList[i] - yEstimates[i]), 2)
    
    return RSS

def getResiduals(yList, yEstimates):
    residuals = []
    for i in range(len(yList)):
        residuals.append(round(yList[i] - yEstimates[i], 4))
    
    return residuals

def getESS(yList, yEstimates, yBar):
    ESS = 0
    for i in range(len(yList)):
        ESS += math.pow((yEstimates[i] - yBar), 2)
    
    return ESS

def getRSquared():
    return (getESS() / getTSS())