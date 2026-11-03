
import math
import random
from pathlib import Path
from datetime import datetime

NAME = "illya vorobey"
GROUP = "it-31"
YEAR = 2008

print(f"{NAME}, {GROUP}")

# Однакові приклади при кожному запуску
random.seed(YEAR)

# Створення прикладів
number1 = random.choice([121, 144, 169, 196, 225])
number2 = random.randint(3, 6)
number3 = random.randint(20, 80)
number4 = random.randint(5, 10)
number5 = random.randint(100, 500)

examples = [
    (f"sqrt({number1})", math.isqrt(number1)),
    (f"{number2}!", math.factorial(number2)),
    (f"gcd({number3}, {number4})",
     math.gcd(number3, number4)),
    (f"comb({number4}, 2)",
     math.comb(number4, 2)),
    (f"5% of {number5}",
     number5 * 5 // 100)
]

score = 0

# Початок вимірювання часу
start_time = datetime.now()

for index, (question, correct_answer) in enumerate(examples, start=1):
    answer = input(f"{index}) {question} = ")

    try:
        user_answer = int(answer)
    except ValueError:
        user_answer = None

    if user_answer == correct_answer:
        print("   correct")
        score += 1
    else:
        print(f"   wrong, answer: {correct_answer}")

# Кінець вимірювання часу
end_time = datetime.now()
seconds = (end_time - start_time).total_seconds()

print(f"score: {score}/5, time: {seconds:.1f} s")

# Шлях до історії
script_directory = Path(__file__).parent
results_directory = script_directory / "results"
results_directory.mkdir(exist_ok=True)

history_file = results_directory / "history.csv"

# Запис результату
new_file = not history_file.exists()

with history_file.open("a", encoding="utf-8") as file:
    if new_file:
        file.write("# datetime;score;seconds\n")

    file.write(
        f"{end_time:%Y-%m-%d %H:%M};{score};{seconds:.1f}\n"
    )

# Читання історії
attempts = []

with history_file.open("r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        parts = line.split(";")

        try:
            attempt_date = datetime.strptime(
                parts[0], "%Y-%m-%d %H:%M"
            )
            attempt_score = int(parts[1])
            attempt_seconds = float(parts[2])

            attempts.append(
                (attempt_date, attempt_score, attempt_seconds)
            )
        except (ValueError, IndexError):
            continue

# Найкращий результат:
# більше балів, а за рівних балів менше часу
best = max(
    attempts,
    key=lambda item: (item[1], -item[2])
)

best_date, best_score, best_seconds = best

print(
    f"attempts: {len(attempts)}, "
    f"best: {best_score}/5 in {best_seconds:.1f} s "
    f"({best_date:%Y-%m-%d %H:%M})"
)
