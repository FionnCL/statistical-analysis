import LinearRegressionModel as LRM

# To use, go to LinearRegressionModel.py and input your points in x[] and y[].
# Save, and come back here and input your new dependent variables below:

dependentVariables = [1.2]

print("\n")
# NOTE: The dependentVariables are for x values!!!
for i in range(len(dependentVariables)):
    currentPredictedVariable = LRM.alpha + (LRM.beta * dependentVariables[i])
    print("Variable x" + (str)(i + 1) + ": " + (str)(currentPredictedVariable))