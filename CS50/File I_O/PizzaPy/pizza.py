import sys
import csv
from tabulate import tabulate

try:
    if len(sys.argv) > 2 or len(sys.argv) == 1\
    or not sys.argv[1].endswith(".csv"):
        sys.exit("Please input only 1 command-line argument"
                  " which is a csv file (ending with.csv)")

    with open(sys.argv[1], "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            first_line = row
            break
        print(tabulate(csvreader,
                    headers=first_line,
                    tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File not found")
