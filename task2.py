
import json
from datetime import date

NAME = "Vorobey Illya"
GROUP = "IT-31"

print(f"{NAME}, {GROUP}")

input_file = "data/expenses.json"
output_file = "data/expenses_updated.json"

# Читаємо JSON
with open(input_file, "r", encoding="utf-8") as file:
    records = json.load(file)

# Додаємо нову витрату
new_record = {
    "date": date.today().isoformat(),
    "category": "food",
    "amount": 10.0,
    "comment": "New personal expense"
}

records.append(new_record)
added = 1

# Видаляємо записи із сумою менше 10
old_count = len(records)

records = [
    record for record in records
    if float(record["amount"]) >= 10
]

deleted = old_count - len(records)

# Записуємо результат в окремий файл
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(
        records,
        file,
        indent=2,
        ensure_ascii=False
    )

print(f"added: {added}")
print(f"deleted: {deleted}")
print(f"saved: {output_file}")
