
import vorobey_files

directory = "."

print("Список файлів у директорії:")
files = vorobey_files.list_files(directory)

for file in files:
    print(file)

substring = "main"

print("\nФайли, які містять підрядок:", substring)

found_files = vorobey_files.find_files(directory, substring)

for file in found_files:
    print(file)

text = """Ім'я: illya
Прізвище: vorobey
Група:it-31
"""

vorobey_files.create_file("student.txt", text)

print("\nФайл student.txt успішно створено!")
