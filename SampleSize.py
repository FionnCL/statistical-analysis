import math

maxWidthOfCI = 0    # funny symbol
variance = 0        # sigma(whatever they say variance is)
zScore = 0          # alpha / 2

def getSampleSize(maxWidthOfCI, variance, zScore):
    return math.pow(((2 * zScore * variance) / maxWidthOfCI), 2)

print("Sample Size:\t" + (str)(getSampleSize(maxWidthOfCI, variance, zScore)))