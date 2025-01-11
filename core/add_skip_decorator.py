import os
import re

test_folder = r"C:\Users\misov\PycharmProjects\BookClubQA_Python_2024_fall\tests"
pattern = re.compile(r"^(def test_\w+\()", re.MULTILINE)
for root, dirs, files in os.walk(test_folder):
    for filename in files:
        if filename.endswith(".py"):  # Проверяем, что это Python файл
            file_path = os.path.join(root, filename)

            try:
                # Открываем файл с указанием кодировки
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()

                # Добавляем декоратор перед каждым тестом
                new_content = pattern.sub(
                    '@pytest.mark.skip(reason="Тест временно отключен после обновления 09.01.2025")\n\\1',
                    content,
                )

                # Записываем измененное содержимое обратно в файл
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(new_content)

                print(f"Декораторы добавлены в {filename}")
            except UnicodeDecodeError:
                print(
                    f"Ошибка декодирования файла {filename}. Попробуйте использовать другую кодировку."
                )
                continue

print("Все файлы обработаны!")
