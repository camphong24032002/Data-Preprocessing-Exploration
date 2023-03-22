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
    missingAttr = data.missingAttribute()
    print(f"The dataset has {len(missingAttr)} attribute(s) with missing value")
    for attr in missingAttr.keys():
        print(f"{attr}: {missingAttr[attr]}")
except (FileNotFoundError) as e:
    print(e)