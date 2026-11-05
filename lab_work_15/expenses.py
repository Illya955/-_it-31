
import csv


def parse_line(line):
    """Перетворює рядок CSV на словник."""
    parts = line.strip().split(";")

    if len(parts) != 4:
        raise ValueError("Рядок повинен містити 4 поля")

    try:
        amount = float(parts[2])
    except ValueError:
        raise ValueError("Сума повинна бути числом")

    return {
        "date": parts[0],
        "category": parts[1],
        "amount": amount,
        "comment": parts[3]
    }


def total_by_category(records):
    """Обчислює загальну суму витрат за категоріями."""
    totals = {}

    for record in records:
        category = record["category"]
        amount = record["amount"]

        totals[category] = totals.get(category, 0) + amount

    return {
        category: round(total, 2)
        for category, total in totals.items()
    }


def load_expenses(path):
    """Завантажує витрати з CSV-файлу."""
    records = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            records.append(parse_line(line))

    return records
