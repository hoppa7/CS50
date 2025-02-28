import csv
import sys

new_names = {}
rows = []

try:
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments") 
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Must be a csv file(ending with .csv)")

    with open(sys.argv[1], "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            first_name = row["name"].split(",")[0]
            last_name = row["name"].split(", ")[1]
            the_row = {
                "first_name": first_name,
                "last_name": last_name,
                "house": row["house"]
                }
            rows.append(the_row)

    fieldnames = ["first_name", "last_name", "house"]

    with open(sys.argv[2], "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
except FileNotFoundError:
    sys.exit("File not found")
