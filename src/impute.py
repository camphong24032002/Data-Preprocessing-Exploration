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
parser.add_argument("--method",
                    action="store",
                    choices=['mean', 'median', 'mode'],
                    required=True,
                    type=str,
                    )
parser.add_argument("--columns",
                    action="store",
                    required=True,
                    type=str,
                    nargs='+',
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
method = args["method"]
columns = args["columns"]

# main
try:
    data = readCSV(inputPath)
    for column in columns:
        if column not in data.getAttributes():
            raise ValueError(f"The attribute {column} is not found")
        data.fillMissing(column, method)
    exportCSV(outputPath, data)
except (FileNotFoundError) as e:
    print(e)