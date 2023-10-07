import os
import json
import shutil
from zipfile import ZipFile

# Сигнатура для формата архива
ARCHIVE_SIGNATURE = b'MYARCH'

# Кодер для нескольких файлов (включая папки)
def encode_files(input_paths, output_archive):
    # Создаем заголовок архива
    archive_header = {
        "signature": ARCHIVE_SIGNATURE,
        "version": 1,  # Версия формата
        "compression_algorithm": 0,  # Алгоритм сжатия: 0 - отсутствие сжатия
        "files": []  # Список файлов и папок в архиве
    }

    # Создаем временную директорию для архивации
    temp_directory = "temp_archive"
    os.makedirs(temp_directory, exist_ok=True)

    try:
        for input_path in input_paths:
            if os.path.isfile(input_path):
                # Если это файл, копируем его во временную директорию
                shutil.copy2(input_path, os.path.join(temp_directory, os.path.basename(input_path)))
                archive_header["files"].append({"type": "file", "path": os.path.basename(input_path)})
            elif os.path.isdir(input_path):
                # Если это папка, копируем её и её содержимое во временную директорию
                shutil.copytree(input_path, os.path.join(temp_directory, os.path.basename(input_path)))
                archive_header["files"].append({"type": "dir", "path": os.path.basename(input_path)})

        # Архивируем временную директорию
        with ZipFile(output_archive, 'w') as zipf:
            for root, _, files in os.walk(temp_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, temp_directory)
                    zipf.write(file_path, arcname=rel_path)

        # Добавляем заголовок архива в начало архивного файла
        with open(output_archive, 'r+b') as archive_file:
            archive_header_json = json.dumps(archive_header).encode('utf-8')
            archive_file.seek(0)
            archive_file.write(archive_header_json)

    finally:
        # Удаляем временную директорию
        shutil.rmtree(temp_directory)

# Декодер для нескольких файлов (включая папки)
def decode_files(input_archive, output_directory):
    # Проверяем сигнатуру архива
    with open(input_archive, 'rb') as archive_file:
        signature = archive_file.read(len(ARCHIVE_SIGNATURE))
        if signature != ARCHIVE_SIGNATURE:
            print("Ошибка: Некорректная сигнатура архива")
            return

    # Извлекаем заголовок архива
    with open(input_archive, 'rb') as archive_file:
        archive_header_json = archive_file.read()
        archive_header = json.loads(archive_header_json.decode('utf-8'))

    # Создаем выходную директорию
    os.makedirs(output_directory, exist_ok=True)

    # Извлекаем содержимое архива
    with ZipFile(input_archive, 'r') as zipf:
        for file_info in archive_header["files"]:
            file_type = file_info["type"]
            file_path = file_info["path"]
            if file_type == "file":
                zipf.extract(file_path, output_directory)
            elif file_type == "dir":
                dir_path = os.path.join(output_directory, file_path)
                os.makedirs(dir_path, exist_ok=True)

# Пример использования кодера и декодера для нескольких файлов и папок
def main():
    input_paths = ["file1.txt", "dir1", "file2.txt"]  # Замените на пути к вашим файлам и папкам
    output_archive = "archive.zip"  # Замените на путь к выходному архивному файлу
   
