import struct
import zlib

# Ваша сигнатура и версия формата
signature = b'\x1A\x2B\x3C\x4D'
version = (1, 0)

# Код алгоритма сжатия
compression_algorithm = 4

# Исходный файл и его содержимое
input_file_name = "input.txt"
with open(input_file_name, "rb") as input_file:
    original_data = input_file.read()
    original_length = len(original_data)

# Сжатие данных
compressed_data = zlib.compress(original_data, level=zlib.Z_BEST_COMPRESSION)

# Создание архива
archive_file_name = "archive.bin"
with open(archive_file_name, "wb") as archive_file:
    # Записываем заголовок
    archive_file.write(signature)
    archive_file.write(struct.pack('!HH', version[0], version[1]))
    archive_file.write(struct.pack('!B', compression_algorithm))
    archive_file.write(struct.pack('!Q', original_length))
    
    # Записываем сжатые данные
    archive_file.write(compressed_data)

# Декодирование архива
with open(archive_file_name, "rb") as archive_file:
    # Чтение заголовка
    file_signature = archive_file.read(4)
    file_version_major, file_version_minor = struct.unpack('!HH', archive_file.read(4))
    file_compression_algorithm = struct.unpack('!B', archive_file.read(1))[0]
    file_original_length = struct.unpack('!Q', archive_file.read(8))[0]
    
    # Проверка сигнатуры и версии
    if file_signature != signature:
        print("Ошибка: Не совпадает сигнатура")
    elif (file_version_major, file_version_minor) != version:
        print("Ошибка: Не поддерживаемая версия")
    elif file_compression_algorithm != compression_algorithm:
        print(f"Ошибка: Неподдерживаемый код алгоритма сжатия ({file_compression_algorithm})")
    else:
        # Если код алгоритма соответствует сжатию, декомпрессируем данные
        decoded_data = zlib.decompress(archive_file.read())
        if len(decoded_data) == file_original_length:
            # Записываем раскодированные данные в новый файл
            decoded_file_name = "decoded.txt"
            with open(decoded_file_name, "wb") as decoded_file:
                decoded_file.write(decoded_data)
            print("Декодирование завершено.")
        else:
            print("Ошибка: Длина раскодированных данных не совпадает с ожидаемой.")
