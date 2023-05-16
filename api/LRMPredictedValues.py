import LinearRegressionModel as LRM

# To use, go to LinearRegressionModel.py and input your points in x[] and y[].
# Save, and come back here and input your new dependent variables below:

# dependentVariables = [1.2]

def getValues(dependentVariables, alpha, beta):
    predictedValues = []
    for i in range(len(dependentVariables)):
        currentPredictedVariable = alpha + (beta * dependentVariables[i])
        predictedValues.append(round(currentPredictedVariable, 4))

    return predictedValues