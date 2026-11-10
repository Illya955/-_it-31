
import csv
import json
import os

NAME = "Vorobey Illya"
GROUP = "IT-31"

print(f"{NAME}, {GROUP}")

input_file = "data/expenses.csv"
output_file = "data/expenses.json"

records = []

with open(input_file, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file, delimiter=";")

    # Прибираємо символ # із назви першого стовпця
    reader.fieldnames = [
        name.lstrip("# ").strip()
        for name in reader.fieldnames
    ]

    for row in reader:
        records.append({
            "date": row["date"],
            "category": row["category"],
            "amount": float(row["amount"]),
            "comment": row["note"]
        })

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(
        records,
        file,
        indent=2,
        ensure_ascii=False
    )

size = os.path.getsize(output_file)

print(f"records: {len(records)}")
print(f"saved: {output_file} ({size} bytes)")
