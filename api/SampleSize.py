import math

def getSampleSize(maxWidthOfCI, variance, zScore):
    return round(math.pow(((2 * zScore * variance) / maxWidthOfCI), 2), 4)