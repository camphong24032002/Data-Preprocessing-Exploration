import sys
import argparse
from Data import *
from File import *

# create parser
parser = argparse.ArgumentParser()

# add arguments
parser.add_argument("path",
                    action="store",
                    type=str,
                    help="csv file's path"
                    )
parser.add_argument("--axis",
                    action="store",
                    choices=['sample', 'attribute'],
                    required=True,
                    type=str,
                    )
parser.add_argument("--threshold",
                    action="store",
                    required=True,
                    type=str,
                    default='0.5',
                    )
parser.add_argument("--out",
                    action="store",
                    required=True,
                    type=str,
                    )

# extract arguments
args = vars(parser.parse_args())
inputPath = args["path"]
outputPath = args["out"]
axis = args["axis"]
threshold = args["threshold"]

#functions
def processThreshold(threshold):
    try:
        value = float(threshold)
    except:
        raise argparse.ArgumentTypeError(f"The value must be float")
    if value < 0 or value > 1:
        raise ValueError(f"The value must be in range [0, 1]")
    return value

# main
try:
    data = readCSV(inputPath)
    threshold=processThreshold(threshold)
    if axis == "sample":
        data.dropSamples(threshold)
    else:
        data.dropAttributes(threshold)
    exportCSV(outputPath, data)
except (FileNotFoundError) as e:
    print(e)