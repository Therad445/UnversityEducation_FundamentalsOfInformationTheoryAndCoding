import os
import json
import shutil
from zipfile import ZipFile

# Сигнатура для формата архива
ARCHIVE_SIGNATURE = b'MYARCH'

# Кодер для нескольких файлов (без папок)
def encode_files(input_paths, output_archive):
    # Создаем заголовок архива
    archive_header = {
        "signature": ARCHIVE_SIGNATURE,
        "version": 1,  # Версия формата
        "compression_algorithm": 0  # Алгоритм сжатия: 0 - отсутствие сжатия
    }

    # Создаем временную директорию для архивации
    temp_directory = "temp_archive"
    os.makedirs(temp_directory, exist_ok=True)

    try:
        for input_path in input_paths:
            # Если это файл, копируем его во временную директорию
            if os.path.isfile(input_path):
                shutil.copy2(input_path, os.path.join(temp_directory, os.path.basename(input_path)))

        # Архивируем временную директорию
        with ZipFile(output_archive, 'w') as zipf:
            for root, dirs, files in os.walk(temp_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, temp_directory)
                    zipf.write(file_path, arcname=rel_path)

    finally:
        # Удаляем временную директорию
        shutil.rmtree(temp_directory)

# Декодер для нескольких файлов (без папок)
def decode_files(input_archive, output_directory):
    # Проверяем сигнатуру архива
    with open(input_archive, 'rb') as archive_file:
        signature = archive_file.read(len(ARCHIVE_SIGNATURE))
        if signature != ARCHIVE_SIGNATURE:
            print("Ошибка: Некорректная сигнатура архива")
            return

    # Извлекаем содержимое архива
    with ZipFile(input_archive, 'r') as zipf:
        zipf.extractall(output_directory)

# Пример использования кодера и декодера для нескольких файлов
def main():
    input_paths = ["file1.txt", "file2.txt"]  # Замените на пути к вашим файлам
    output_archive = "archive.zip"  # Замените на путь к выходному архивному файлу
    output_directory = "output_directory"  # Замените на путь к выходной директории для декодирования

    # Кодирование файлов
    encode_files(input_paths, output_archive)

    # Декодирование файлов
    decode_files(output_archive, output_directory)

if __name__ == "__main__":
    main()

