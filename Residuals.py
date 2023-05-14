import LinearRegressionModel as LRM
import math

# To use, go to LinearRegressionModel.py and input your points in x[] and y[].
# Save, and come back here and input your new dependent variables below:

print("\n")

def getEstimatedY():
    yEstimates = []
    for i in range(len(LRM.xList)):
        yEstimates.append(LRM.alpha + (LRM.beta * LRM.xList[i]))

    return yEstimates

def getTSS():
    TSS = 0
    for i in range(len(LRM.yList)):
        TSS += math.pow((LRM.yList[i] - LRM.yBar), 2)
    
    return TSS

def getRSS():
    RSS = 0
    yEstimates = getEstimatedY()
    for i in range(len(LRM.yList)):
        RSS += math.pow((LRM.yList[i] - yEstimates[i]), 2)
    
    return RSS

def getResiduals():
    residuals = []
    yEstimates = getEstimatedY()
    for i in range(len(LRM.yList)):
        residuals.append(LRM.yList[i] - yEstimates[i])
    
    return residuals

def getESS():
    ESS = 0
    yEstimates = getEstimatedY()
    for i in range(len(LRM.yList)):
        ESS += math.pow((yEstimates[i] - LRM.yBar), 2)
    
    return ESS

def getRSquared():
    return (getESS() / getTSS())

print("--------------------")
print("TSS is n * the sample variance of Y.")
print("RSS is n * the sample variance of residuals.")
print("ESS is n * the sample variance of the fitted values.")
print("R Squared = correlation squared.")
print("Note: Read notes if asked about these. On BlackBoard.")
print("--------------------")
print("TSS: " + (str)(getTSS()))
print("RSS: " + (str)(getRSS()))
print("ESS: " + (str)(getESS()))
print("R Squared: " + (str)(getRSquared()))
print("--------------------")