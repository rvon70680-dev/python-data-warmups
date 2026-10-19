import csv

counts = {}

with open("trades.csv", "r") as file:
    for row in csv.DictReader(file):
        symbol = row["desk"]
        counts[symbol] = counts.get(symbol, 0) + 1
print(counts)
