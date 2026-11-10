
import json
from datetime import date

NAME = "Vorobey Illya"
GROUP = "IT-31"

print(f"{NAME}, {GROUP}")

# Початкові дані
original = {
    "owner": NAME,
    "created": date.today(),
    "category": "food"
}

# 1. Спроба звичайної серіалізації
try:
    json.dumps(original)
except TypeError as error:
    print("TypeError:", error)


# 2. Використання параметра default=
def date_serializer(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} is not serializable")


json_text = json.dumps(original, default=date_serializer)
print("Using default:", json_text)


# 3. Власна функція перетворення дат
def prepare_for_json(data):
    if isinstance(data, date):
        return {"__date__": data.isoformat()}

    if isinstance(data, dict):
        return {
            key: prepare_for_json(value)
            for key, value in data.items()
        }

    if isinstance(data, list):
        return [prepare_for_json(item) for item in data]

    return data


# Відновлення дат
def restore_dates(data):
    if isinstance(data, dict):
        if set(data.keys()) == {"__date__"}:
            return date.fromisoformat(data["__date__"])

        return {
            key: restore_dates(value)
            for key, value in data.items()
        }

    if isinstance(data, list):
        return [restore_dates(item) for item in data]

    return data


# Записуємо JSON
prepared = prepare_for_json(original)

with open("dates.json", "w", encoding="utf-8") as file:
    json.dump(prepared, file, indent=2, ensure_ascii=False)

# Читаємо JSON
with open("dates.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

# Відновлюємо початкові типи
restored = restore_dates(loaded)

print("Restored:", restored)
print("Equal:", restored == original)
print("Date type:", type(restored["created"]))

assert restored == original
assert isinstance(restored["created"], date)
