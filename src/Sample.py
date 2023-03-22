class Sample:

    """
    Attribute:
        data: a dictionary, contains the value of attribute with attribute as key        
    """

    """
    Initialize the Sample object

    Args:
        attributes: a list of string, the attribute list
        values: a list of string, the value list corresponding to the attribute list
    """
    def __init__(self, attributes, values = []):
        self.data = dict()
        for attr, val in zip(attributes, values):
            # Try to cast the numeric value
            try:
                self.data[attr] = float(val)
            except:
                self.data[attr] = val

    """
    Compare two sample

    Args:
        sample: the comparing sample
    Returns:
        result: a boolean value
    """
    def __eq__(self, sample):
        selfAttr = self.getAttributes()
        otherAttr = sample.getAttributes()
        # check if they have the same length of attributes
        if (len(selfAttr) != len(otherAttr)):
            return False
        for attr in selfAttr:
            # check if they have the same attributes
            if attr not in otherAttr:
                return False
            # check if they have the same values
            if self.getValue(attr) != sample.getValue(attr):
                return False
        return True

    """
    Get a value corresponding to the given attribute

    Args:
        attribute: a string, a request attribute
    Returns:
        value: a string or float, a request value
    """
    def getValue(self, attribute):
        return self.data[attribute]
    
    """
    Get the list of attributes

    Returns:
        list: a list of string, the attribute list
    """
    def getAttributes(self):
        return self.data.keys()
    
    """
    Get the list of missing attribute

    Returns:
        list: a list of string, the missing attribute list
    """
    def getMissingAttribute(self):
        result = []
        for attr in self.data.keys():
            if self.data[attr] == "":
                result.append(attr)
        return result
    
    """
    Set value of the attribute

    Args:
        attribute: a string, an attribute we want to change
        value: a string or float, a value we want to set 
    """
    def setValue(self, attribute, value):
        self.data[attribute] = value
    
    """
    Drop attribute of the sample

    Args:
        attribute: a string, an attribute we want to drop
    """
    def dropAttribute(self, attribute):
        del self.data[attribute]