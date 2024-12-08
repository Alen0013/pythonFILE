import os

# 1. Получение нормализованного абсолютного пути к файлу test_file_1.txt
file_1_path = os.path.abspath('data_path_1/test_file_1.txt')
print("Нормализованный абсолютный путь к test_file_1.txt:", file_1_path)

# 2. Вывод содержимого папки проекта с помощью os.walk()
print("\nСодержимое папки проекта:")
for dirpath, dirnames, filenames in os.walk('.'):
    print(f'Папка: {dirpath}')
    for filename in filenames:
        print(f' - Файл: {filename}')

# 3. Составление нормализованного абсолютного пути к файлу test_file_3.txt
file_3_path = os.path.join(os.path.abspath('data_path_2'), 'test_file_3.txt')
print("\nНормализованный абсолютный путь к test_file_3.txt:", file_3_path)

# 4. Код для создания и удаления папки внутри data_path_2
new_folder_path = os.path.join('data_path_2', 'new_folder')

# Создание новой папки
os.makedirs(new_folder_path)
print(f"\nСоздана папка: {new_folder_path}")

# Удаление новой папки
os.rmdir(new_folder_path)
print(f"Удалена папка: {new_folder_path}")
