import math

"""
Get mean of the value list

Args:
    values: a list of float, the value list
Returns:
    result: a float, the mean of the value list
"""
def getMean(values):
    num = len(values)
    # in case list of values is null
    if num == 0:
        return 0
    return sum(values)/len(values)

"""
Get median of the value list

Args:
    values: a list of float, the value list
Returns:
    result: a float, the median of the value list
"""
def getMedian(values):
    num = len(values)
    # in case list of values is null
    if num == 0:
        return 0
    values = sorted(values)
    mid = num//2
    if num%2:
        return values[mid]
    return (values[mid]+values[mid-1])/2

"""
Get mode of the value list

Args:
    values: a list of float, the value list
Returns:
    result: a string or float, the median of the value list
"""
def getMode(values):
    freq = dict()
    if values == []:
        return None
    for value in values:
        if value in freq:
            freq[value] += 1
        else:
            freq[value] = 1
    return max(freq, key=freq.get)

"""
Get standard deviation of the value list

Args:
    values: a list of float, the value list
Returns:
    result: a list of float, the standard deviation of the value list
"""
def getStd(values):
    numValue = len(values)
    mean = getMean(values)
    std = 0
    for value in values:
        std += (value-mean)**2
    std = math.sqrt(std/numValue)
    return std

"""
Calculate the value of Min-Max Normalization

Args:
    value: a float, the normalizing value
    minVal: a float, the min value of the list
    maxVal: a float, the max value of the list
Returns:
    result: a float, the value after normalizing
"""
def normalizeMinMax(value, minVal, maxVal):
    return (value-minVal)/(maxVal-minVal)

"""
Calculate the value of Standard Deviation Normalization

Args:
    value: a float, the normalizing value
    mean: a float, the mean value of the list
    std: a float, the standard deviation value of the list
Returns:
    result: a float, the value after normalizing
"""
def normalizeZScore(value, mean, std):
    return (value-mean)/std