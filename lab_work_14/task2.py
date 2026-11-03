
import csv
from collections import defaultdict
from decimal import Decimal
from tabulate import tabulate

print("Illya Vorobey, IT-31")

categories = defaultdict(lambda: [0, Decimal("0.00")])

with open("data/expenses.csv", encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        if not row or row[0].strip().startswith("#"):
            continue

        if len(row) < 3:
            continue

        category = row[1].strip()
        amount = Decimal(row[2].strip())

        categories[category][0] += 1
        categories[category][1] += amount

table = []
total_count = 0
total_amount = Decimal("0.00")

for category, values in categories.items():
    count, amount = values

    table.append([category, count, f"{amount:.2f}"])

    total_count += count
    total_amount += amount

table.append(["TOTAL", total_count, f"{total_amount:.2f}"])

print(tabulate(
    table,
    headers=["category", "count", "total"],
    tablefmt="github",
    disable_numparse=True
))