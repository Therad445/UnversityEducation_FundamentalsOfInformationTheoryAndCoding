import struct

# Ваша сигнатура и версия формата
signature = b'\x1A\x2B\x3C\x4D'
version = (1, 0)

# Коды алгоритмов сжатия и защиты (начнем с отсутствия сжатия и защиты)
compression_algorithm = 0
error_correction_algorithm = 0

# Исходный файл и его содержимое
input_file_name = "input.txt"
with open(input_file_name, "rb") as input_file:
    original_data = input_file.read()
    original_length = len(original_data)

# Создание архива
archive_file_name = "archive.bin"
with open(archive_file_name, "wb") as archive_file:
    # Записываем заголовок
    archive_file.write(signature)
    archive_file.write(struct.pack('!HH', version[0], version[1]))
    archive_file.write(struct.pack('!BB', compression_algorithm, error_correction_algorithm))
    archive_file.write(struct.pack('!Q', original_length))
    
    # Записываем несжатые данные
    archive_file.write(original_data)

# Декодирование архива
with open(archive_file_name, "rb") as archive_file:
    # Чтение заголовка
    file_signature = archive_file.read(4)
    file_version_major, file_version_minor = struct.unpack('!HH', archive_file.read(4))
    file_compression_algorithm, file_error_correction_algorithm = struct.unpack('!BB', archive_file.read(2))
    file_original_length = struct.unpack('!Q', archive_file.read(8))[0]
    
    # Проверка сигнатуры и версии
    if file_signature != signature:
        print("Ошибка: Не совпадает сигнатура")
    elif (file_version_major, file_version_minor) != version:
        print("Ошибка: Не поддерживаемая версия")
    else:
        # Если коды алгоритмов соответствуют отсутствию сжатия и защиты,
        # восстанавливаем исходный файл
        if file_compression_algorithm == 0 and file_error_correction_algorithm == 0:
            decoded_data = archive_file.read()
            if len(decoded_data) == file_original_length:
                # Записываем раскодированные данные в новый файл
                decoded_file_name = "decoded.txt"
                with open(decoded_file_name, "wb") as decoded_file:
                    decoded_file.write(decoded_data)
                print("Декодирование завершено.")
            else:
                print("Ошибка: Длина раскодированных данных не совпадает с ожидаемой.")
        else:
            print("Ошибка: Поддерживаются только алгоритмы без сжатия и защиты.")
