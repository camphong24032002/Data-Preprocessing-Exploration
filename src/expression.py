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
parser.add_argument("--expression",
                    action="store",
                    choices=['addition', 'subtraction', 'multiplication', 'division'],
                    required=True,
                    type=str,
                    )
parser.add_argument("--columns",
                    action="store",
                    required=True,
                    nargs=2,
                    type=str,
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
expression = args["expression"]
columns = args["columns"]

# main
try:
    data = readCSV(inputPath)
    # check if the column is an attribute
    for column in columns:
        if column not in data.getAttributes():
            raise ValueError(f"The attribute {column} is not found")
    values = data.attributeExpression(columns[0], columns[1], expression)
    data.addAttribute(expression, values)
    exportCSV(outputPath, data)
except (FileNotFoundError) as e:
    print(e)