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
parser.add_argument("--out",
                    action="store",
                    required=True,
                    type=str,
                    )

# extract arguments
args = vars(parser.parse_args())
inputPath = args["path"]
outputPath = args["out"]

# main
try:
    data = readCSV(inputPath)
    data.dropDuplicates()
    exportCSV(outputPath, data)
except (FileNotFoundError) as e:
    print(e)