
import math
import sys
from pathlib import Path
from datetime import date, timedelta

NAME = "illya vorobey"
GROUP = "it-31"

print(f"{NAME}, {GROUP}")

# Шлях до файлу
file_path = Path(__file__).parent / "data" / "expenses.csv"

expenses = []

# Читання файлу
try:
    with file_path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split(";")

            if len(parts) != 4:
                print(
                    f"Warning: incorrect line {line_number}",
                    file=sys.stderr
                )
                continue

            try:
                expense_date = date.fromisoformat(parts[0])
                amount = float(parts[2])

                if amount < 0:
                    raise ValueError

                expenses.append((expense_date, amount))

            except ValueError:
                print(
                    f"Warning: invalid line {line_number}",
                    file=sys.stderr
                )

except FileNotFoundError:
    print("Error: expenses.csv not found", file=sys.stderr)
    sys.exit(1)

if not expenses:
    print("Error: no valid expenses", file=sys.stderr)
    sys.exit(1)

# Сортування
expenses.sort(key=lambda x: x[0])

first_date = expenses[0][0]
last_date = expenses[-1][0]

period_days = (last_date - first_date).days + 1

print(
    f"period: {first_date:%d.%m.%Y} ({first_date:%A}) - "
    f"{last_date:%d.%m.%Y} ({last_date:%A}), "
    f"{period_days} days"
)

# Суми за днями тижня
weekday_totals = [0.0] * 7
daily_totals = {}

current = first_date

while current <= last_date:
    daily_totals[current] = 0.0
    current += timedelta(days=1)

for expense_date, amount in expenses:
    daily_totals[expense_date] += amount
    weekday_totals[expense_date.weekday()] += amount

weekdays = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

print("\nweekday      total")

for i in range(7):
    print(f"{weekdays[i]:<12} {weekday_totals[i]:8.2f}")

# Загальна статистика
total = math.fsum(amount for _, amount in expenses)

average = total / period_days

variance = math.fsum(
    (amount - average) ** 2
    for amount in daily_totals.values()
) / period_days

std_dev = math.sqrt(variance)

top_day = max(daily_totals, key=daily_totals.get)

no_spend_days = sum(
    1 for amount in daily_totals.values()
    if amount == 0
)

print(f"\ntotal:        {total:.2f}")
print(f"per day:      {average:.2f} +- {std_dev:.2f}")

print(
    f"top day:      {top_day:%d.%m.%Y} "
    f"({top_day:%A}), {daily_totals[top_day]:.2f}"
)

print(f"no-spend days: {no_spend_days}")

# Кількість днів у місяці
month_start = last_date.replace(day=1)

if last_date.month == 12:
    next_month = date(last_date.year + 1, 1, 1)
else:
    next_month = date(last_date.year, last_date.month + 1, 1)

days_in_month = (next_month - month_start).days
days_left = (next_month - last_date).days

forecast = total / period_days * days_in_month

print(
    f"days in {last_date.strftime('%B')}: "
    f"{days_in_month}, left after {last_date:%d.%m}: {days_left}"
)

print(f"month forecast: {forecast:.2f}")

# Перевірка переходу року та високосного року
december_days = (
    date(2027, 1, 1) - date(2026, 12, 1)
).days

february_days = (
    date(2028, 3, 1) - date(2028, 2, 1)
).days

print(f"\nDecember 2026 days: {december_days}")
print(f"February 2028 days: {february_days}")
