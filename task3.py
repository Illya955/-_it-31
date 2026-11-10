
import json
import sys
import os

NAME = "Vorobey Illya"
GROUP = "IT-31"

print(f"{NAME}, {GROUP}")

settings_file = "settings.json"
expenses_file = "data/expenses.json"

default_settings = {
    "owner": NAME,
    "group": GROUP,
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"]
}

# Перевіряємо наявність файлу
if not os.path.exists(settings_file):
    with open(settings_file, "w", encoding="utf-8") as file:
        json.dump(
            default_settings,
            file,
            indent=2,
            ensure_ascii=False
        )

    print("settings.json not found, default created")
    sys.exit(0)

# Читаємо налаштування та обробляємо помилки
try:
    with open(settings_file, "r", encoding="utf-8") as file:
        settings = json.load(file)

except json.JSONDecodeError as error:
    print(
        f"JSON error at line {error.lineno}: {error.msg}",
        file=sys.stderr
    )
    sys.exit(1)

# Читаємо витрати
with open(expenses_file, "r", encoding="utf-8") as file:
    expenses = json.load(file)

spent = sum(float(item["amount"]) for item in expenses)

limit = float(settings["monthly_limit"])
left = limit - spent

print("Owner:", settings["owner"])
print("Group:", settings["group"])
print("Categories:", settings["categories"])

print(
    f"limit: {limit:.2f} {settings['currency']}, "
    f"spent: {spent:.2f} {settings['currency']}, "
    f"left: {left:.2f} {settings['currency']}"
)
