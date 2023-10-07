import os
import struct

# Ваша сигнатура и версия формата
signature = b'\x1A\x2B\x3C\x4D'
version = (1, 0)

# Коды алгоритмов сжатия и защиты (начнем с отсутствия сжатия и защиты)
compression_algorithm = 0
error_correction_algorithm = 0

# Каталог для архивации и декодирования
base_dir = "my_directory"

# Создание архива
archive_file_name = "archive.bin"

def archive_directory(directory_path, archive_file):
    for root, dirs, files in os.walk(directory_path):
        # Записываем относительный путь от базовой директории
        relative_path = os.path.relpath(root, directory_path)
        archive_file.write(struct.pack('!H', len(relative_path)))
        archive_file.write(relative_path.encode('utf-8'))
        
        # Записываем количество файлов и поддиректорий
        archive_file.write(struct.pack('!H', len(files)))
        archive_file.write(struct.pack('!H', len(dirs)))
        
        # Записываем файлы
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, "rb") as input_file:
                original_data = input_file.read()
                original_length = len(original_data)
                # Записываем имя файла и его длину
                archive_file.write(struct.pack('!H', len(file_name)))
                archive_file.write(file_name.encode('utf-8'))
                archive_file.write(struct.pack('!Q', original_length))
                # Записываем несжатые данные
                archive_file.write(original_data)

archive_file_name = "archive.bin"
with open(archive_file_name, "wb") as archive_file:
    # Записываем заголовок
    archive_file.write(signature)
    archive_file.write(struct.pack('!HH', version[0], version[1]))
    archive_file.write(struct.pack('!BB', compression_algorithm, error_correction_algorithm))
    
    # Архивируем каталог
    archive_directory(base_dir, archive_file)

print("Архивация завершена.")

# Декодирование архива
def create_directory(directory_path):
    os.makedirs(directory_path, exist_ok=True)

def decode_directory(base_dir, archive_file):
    while True:
        # Читаем относительный путь
        path_length = struct.unpack('!H', archive_file.read(2))[0]
        if path_length == 0:
            break
        relative_path = archive_file.read(path_length).decode('utf-8')
        
        # Создаем поддиректории
        directory_path = os.path.join(base_dir, relative_path)
        num_files = struct.unpack('!H', archive_file.read(2))[0]
        num_dirs = struct.unpack('!H', archive_file.read(2))[0]
        
        create_directory(directory_path)
        
        # Создаем файлы
        for _ in range(num_files):
            # Читаем имя файла и его длину
            file_name_length = struct.unpack('!H', archive_file.read(2))[0]
            file_name = archive_file.read(file_name_length).decode('utf-8')
            file_original_length = struct.unpack('!Q', archive_file.read(8))[0]
            # Записываем несжатые данные в файл
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, "wb") as output_file:
                output_file.write(archive_file.read(file_original_length))
        
        # Рекурсивно обрабатываем поддиректории
        for _ in range(num_dirs):
            decode_directory(directory_path, archive_file)

with open(archive_file_name, "rb") as archive_file:
    # Чтение заголовка
    file_signature = archive_file.read(4)
    file_version_major, file_version_minor = struct.unpack('!HH', archive_file.read(4))
    file_compression_algorithm, file_error_correction_algorithm = struct.unpack('!BB', archive_file.read(2))
    
    # Проверка сигнатуры и версии
    if file_signature != signature:
        print("Ошибка: Не совпадает сигнатура")
    elif (file_version_major, file_version_minor) != version:
        print("Ошибка: Не поддерживаемая версия")
    else:
        # Если коды алгоритмов соответствуют отсутствию сжатия и защиты,
        # декодируем файлы
        if file_compression_algorithm == 0 and file_error_correction_algorithm == 0:
            decode_directory(base_dir, archive_file)
            print("Декодирование завершено.")
        else:
            print("Ошибка: Поддерживаются только алгоритмы без сжатия и защиты.")
