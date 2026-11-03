
import sys
import math
from pathlib import Path
from datetime import datetime

NAME = "illya vorobey"
GROUP = "it-31"


def format_size(size):
    """Повертає розмір файлу у зручному форматі."""
    if size == 0:
        return "0 B"

    units = ["B", "KB", "MB", "GB"]
    index = min(int(math.log(size, 1024)), 3)
    value = size / (1024 ** index)

    return f"{value:.1f} {units[index]}"


def main():
    print(f"{NAME}, {GROUP}")

    args = sys.argv[1:]
    dry_run = False

    if args and args[0] == "--dry-run":
        dry_run = True
        args = args[1:]

    if len(args) != 1:
        print(
            "usage: python task3.py [--dry-run] <dir>",
            file=sys.stderr
        )
        sys.exit(2)

    directory = Path(args[0])

    if not directory.exists() or not directory.is_dir():
        print(f"error: {directory} is not a directory", file=sys.stderr)
        sys.exit(1)

    files = [p for p in directory.iterdir() if p.is_file()]

    if not files:
        print("No files found.")
        return

    # Сортування від найстарішого до найновішого
    files.sort(key=lambda p: p.stat().st_mtime)

    plan = []

    for file in files:
        stat = file.stat()
        modified = datetime.fromtimestamp(stat.st_mtime)
        folder_name = modified.strftime("%Y-%m")
        destination = directory / folder_name / file.name

        plan.append((file, destination, stat.st_size, modified))

    # Перевірка всіх конфліктів перед переміщенням
    for file, destination, size, modified in plan:
        if destination.exists():
            print(
                f"error: {destination} already exists, nothing was moved",
                file=sys.stderr
            )
            sys.exit(1)

    # Виведення плану
    for file, destination, size, modified in plan:
        print(
            f"{file.name:<20} {format_size(size):>10}  "
            f"{modified:%d.%m.%Y %H:%M}  -> "
            f"{destination.parent.name}/"
        )

    folders_count = len(set(
        destination.parent for _, destination, _, _ in plan
    ))

    if dry_run:
        print(
            f"{len(plan)} files, {folders_count} folders "
            "(dry run, nothing moved)"
        )
        return

    # Переміщення файлів
    for file, destination, size, modified in plan:
        destination.parent.mkdir(exist_ok=True)
        file.rename(destination)

    # Створення звіту
    script_directory = Path(__file__).parent
    reports_directory = script_directory / "reports"
    reports_directory.mkdir(exist_ok=True)

    now = datetime.now()
    report_path = reports_directory / (
        f"organize_{now:%Y%m%d_%H%M}.txt"
    )

    with report_path.open("w", encoding="utf-8") as report:
        report.write(f"{NAME}, {GROUP}\n")
        report.write(f"Files moved: {len(plan)}\n")

        for file, destination, size, modified in plan:
            report.write(f"{file.name} -> {destination}\n")

    print(f"{len(plan)} files, {folders_count} folders")
    print(f"report saved to: {report_path}")


if __name__ == "__main__":
    main()
