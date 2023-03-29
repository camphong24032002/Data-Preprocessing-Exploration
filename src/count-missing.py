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

# extract arguments
args = vars(parser.parse_args())
inputPath = args["path"]

# main
try:
    data = readCSV(inputPath)
    missingSamples = data.missingSample()
    print(f"There are {data.length()} samples in the dataset")
    print(f"The dataset has {missingSamples} line(s) with missing value")
except (FileNotFoundError) as e:
    print(e)