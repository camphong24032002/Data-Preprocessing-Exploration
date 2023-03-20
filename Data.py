import math
from Sample import *
from Utils import *

class Data:
    """
    Attribute:
        data: a list of dictionary, samples of data frame
        attributes: a list of string, the attribute list
    """
    
    """
    Initialize the data with a list of attributes

    Args:
        attributes: a list of string, the attribute list
    """
    def __init__(self, attributes):
        self.data = []
        self.attributes = attributes.copy()
    
    """
    Get the attribute list
    
    Returns:
        list: a list of string, the attribute list
    """
    def getAttributes(self):
        return self.attributes.copy()
    
    """
    Get value of the given attribute
    
    Args:
        attribute: a string, an attribute we want to extract
    Returns:
        list: a list, values extracted from samples
    """
    def getValues(self, attribute):
        result = []
        for sample in self.data:
            value = sample.getValue(attribute)
            if value == "":
                continue
            result.append(value)
        return result

    """
    Get a sample of data
    
    Args:
        index: an integer number, the index of samples
    Returns:
        list: a list, the sample at requesting index
    """
    def getSample(self, index):
        return self.data[index]
    
    """
    Get the number of samples
    
    Returns:
        number: an integer number, the number of samples
    """
    def length(self):
        return len(self.data)

    """
    Add a sample to data
    
    Args:
        sample: a list, the adding sample
    """
    def addSample(self, sample):
        self.data.append(sample)

    """
    Add a attribute to data

    Args:
        attributeName: a string, the name of attribute
        values: a list, the value of attribute
    """
    def addAttribute(self, attributeName, values):
        self.attributes.append(attributeName)
        for index in range(self.length()):
            # try to cast the numeric value
            try:
                self.getSample(index).setValue(attributeName, float(values[index]))
            except:
                self.getSample(index).setValue(attributeName, values[index])

    """
    Find the missing attributes and count the number of the missing sample

    Returns:
        dict: a dictionary, the missing attribute as key and the number of missing sample as value
    """
    def missingAttribute(self):
        result = dict()
        for attr in self.attributes:
            for sample in self.data:
                if sample.getValue(attr) == "":
                    if attr in result:
                        result[attr] += 1
                    else:
                        result[attr] = 1
        return result
    
    """
    Count the number of missing samples
    
    Returns:
        value: the number of the missing samples
    """
    def missingSample(self):
        count = 0
        for sample in self.data:
            missingAttr = sample.getMissingAttribute()
            if (len(missingAttr) != 0):
                count += 1
        return count

    """
    Fill missing value of an attribute with the given method

    Args:
       attribute: a string, an attribute we want to fill
       method: a string (mean, mode, median), the method we want to apply
    """
    def fillMissing(self, attribute, method):
        method = method.lower()
        
        values = self.getValues(attribute)
        
        for value in values:
            if type(value) == str and method != "mode":
                raise ValueError("Method for numeric attribute must be method=mode")

        fillValue = None
        if method == 'mean':
            fillValue = getMean(values)
        elif method == "median":
            fillValue = getMedian(values)
        elif method == "mode":
            fillValue = getMode(values)
            if fillValue == None:
                if type(value[0]) == str:
                    fillValue = ""
                else:
                    fillValue = 0

        for sample in self.data:
            value = sample.getValue(attribute)
            if value == '':
                sample.setValue(attribute, fillValue)
    
    """
    Drop samples with missing value greater than threshold

    Args:
        threshold: the threshold of the missing values to be removed
    """
    def dropSamples(self, threshold=.5):
        numAttr = len(self.attributes)
        newData = []
        for sample in self.data:
            missingAttr = sample.getMissingAttribute()
            rate = len(missingAttr)/numAttr
            if (rate <= threshold):
                newData.append(sample)
        self.data = newData

    """
    Drop attributes with missing value greater than threshold
    
    Args:
        threshold: the threshold of the missing values to be removed
    """
    def dropAttributes(self, threshold=.5):
        numSample = self.length()
        missingAttr = self.missingAttribute()
        for attr in missingAttr.keys():
            rate = missingAttr[attr]/numSample
            if (rate <= threshold):
                continue
            self.attributes.remove(attr)
            for sample in self.data:
                sample.dropAttribute(attr)

    """
    Drop duplicate samples
    """
    def dropDuplicates(self):
        newData = []
        for sample in self.data:
            if not(sample in newData):
                newData.append(sample)
        self.data = newData

    """
    Normalize the attributes with the given method

    Args:
        attribute: a string, an attribute we want to normalize
        method: a string (min-max, z-score), the method we want to apply
    """
    def normalizeValue(self, attribute, method):
        values = self.getValues(attribute)
        
        for value in values:
            if type(value) == str:
                raise ValueError("The attribute type must be numeric")

        minVal = min(values)
        maxVal = max(values)
        mean = getMean(values)
        std = getStd(values)
        
        normalizeVal = 0
        for sample in self.data:
            value = sample.getValue(attribute)
            if value == "":
                continue
            if method == "min-max":
                normalizeVal = normalizeMinMax(value, minVal, maxVal)
            elif method == "z-score":
                normalizeVal = normalizeZScore(value, mean, std)
            sample.setValue(attribute, normalizeVal)

    """
    Perform expression between two attributes

    Args:
        attribute1: a string, the first attribute
        attribute2: a string, the second attribute
        expression: a string (addition, subtraction, multiplication, division), the type of expression
    Returns:
        list: a list, the value list after applying expression 
    """
    def attributeExpression(self, attribute1, attribute2, expression):
        expression = expression.lower()
        newValue = []
        for sample in self.data:
            value1, value2 = sample.getValue(attribute1), sample.getValue(attribute2)
            if value1 == "" or value2 == "":
                newValue.append("") 
            elif type(value1) == str or type(value2) == str:
                raise ValueError("The attributes must be numeric")
            elif expression == "addition":
                newValue.append(value1+value2)
            elif expression == "subtraction":
                newValue.append(value1-value2)
            elif expression == "multiplication":
                newValue.append(value1*value2)
            elif expression == "division":
                newValue.append(value1/value2)
        return newValue