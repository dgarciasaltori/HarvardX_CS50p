import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if len(sys.argv) == 3:
    extension = sys.argv[1]
    extension = extension.split('.')
    if extension[1] != "csv":
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            with open(sys.argv[2], 'w') as file2:
                writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    row["first"] = row.pop("name")
                    last_name, first_name = row["first"].split(",")
                    row["first"] = first_name
                    row["last"] = last_name
                    writer.writerow(row)
    except FileNotFoundError:
        file_name = sys.argv[1]
        sys.exit("Could not read " + file_name)