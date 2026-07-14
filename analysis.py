import csv
from statistics import mean

with open("data.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    rows = [row for row in reader]

amounts = [float(row["amount"]) for row in rows]
print("Number of rows", len(rows))
print("mean sale amount", mean(amounts))
print("Largest sale amount:", max(amounts))
    