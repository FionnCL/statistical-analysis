import math


observedFrequencies = [
    [6, 3, 3, 1],
    [6, 4, 4, 1],
    [0, 3, 2, 2]
 ]

def getExpectedFrequencies(matrix):
    columnSize = len(matrix)
    rowSize = len(matrix[0])
    expectedFrequencies = [[] * rowSize] * columnSize
    total = getTotal(matrix)

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(round((((getRowTotal(matrix[i]) * getColumnTotal(j, matrix)) / total)), 4))
        expectedFrequencies[i] = row

    return expectedFrequencies


def getRowTotal(row):
    summation = 0
    for i in range(len(row)):
        summation += row[i]
    
    return summation

def getColumnTotal(columnIndex, matrix):
    summation = 0
    for i in range(len(matrix)):
        summation += matrix[i][columnIndex]

    return summation

def getTotal(matrix):
    summation = 0
    for i in range(len(matrix)): 
        summation += getRowTotal(matrix[i])
    
    return summation

def getChiSquared(observedFrequencies, expectedFrequencies):
    summation = 0
    for i in range(len(expectedFrequencies)):
        for j in range(len(expectedFrequencies[i])):
            summation += (math.pow((observedFrequencies[i][j] - expectedFrequencies[i][j]), 2)) / expectedFrequencies[i][j]
    return round(summation, 4)