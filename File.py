from Data import *
from Sample import *

"""
Read a csv file with the given path

Args:
    filepath: a string, the file path
Returns:
    data: a Data object, the dataset loaded from csv file
"""
def readCSV(filepath):
    file = open(filepath, 'r')
    # read the first line as attributes
    attributes = file.readline()
    attributes = attributes.replace("\n", "")
    attributes = attributes.split(',')
    data = Data(attributes)
    # read each line as sample
    for line in file:
        line = line.replace("\n", "")
        sample = Sample(attributes, line.split(','))
        data.addSample(sample)
    file.close()
    return data

"""
Export the dataset to csv file

Args:
    filepath: a string, the file path
    data: a Data object, the dataset we want to export
"""
def exportCSV(filepath, data):
    file = open(filepath, 'w')
    # write attributes to file
    file.write(",".join(data.getAttributes())+"\n")
    # write each sample to file
    for index in range(data.length()):
        sample = data.getSample(index)
        values = []
        for attribute in data.getAttributes():
            values.append(str(sample.getValue(attribute)))
        file.write(",".join(values)+"\n")
    file.close()