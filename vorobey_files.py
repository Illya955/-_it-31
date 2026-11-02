
import os


def list_files(directory):
    """
    Повертає список файлів у вказаній директорії.

    Параметри:
        directory (str): шлях до директорії.

    Результат:
        list: список назв файлів.
    """
    return [
        filename
        for filename in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, filename))
    ]


def find_files(directory, substring):
    """
    Шукає файли, у назві яких є заданий підрядок.

    Параметри:
        directory (str): шлях до директорії.
        substring (str): підрядок для пошуку.

    Результат:
        list: список знайдених файлів.
    """
    return [
        filename
        for filename in list_files(directory)
        if substring in filename
    ]


def create_file(path, text):
    """
    Створює файл із заданим текстом.

    Параметри:
        path (str): шлях до нового файлу.
        text (str): текст для запису.

    Результат:
        str: шлях до створеного файлу.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)

    return path


if __name__ == "__main__":
    print("Перевірка модуля petrenko_files.py")

    directory = "."

    print("Список файлів:", list_files(directory))

    print("Пошук файлів із підрядком 'main':",
          find_files(directory, "main"))

    create_file(
        "test_file.txt",
        "Це тестовий файл для перевірки модуля."
    )

    print("Створено файл:", "test_file.txt")
