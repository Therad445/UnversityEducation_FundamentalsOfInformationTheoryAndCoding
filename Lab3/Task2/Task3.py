import pickle

class HuffmanNode:
    # Определение класса HuffmanNode, как было показано в предыдущих ответах

def decode_huffman(input_file, output_file):
    with open(input_file, 'rb') as file:
        root, compressed_data = pickle.load(file)

    # Ваш код для декомпрессии данных, как было показано в предыдущих ответах

def decode_l1_format(input_file, output_file):
    with open(input_file, 'rb') as file:
        file_signature = file.read(len(signature_l1))  # Замените на сигнатуру Л1
        file_version = int.from_bytes(file.read(1), byteorder='big')
        file_algorithm_code = int.from_bytes(file.read(1), byteorder='big')

        if file_signature != signature_l1 or file_version != version_l1 or file_algorithm_code != 0:
            print("Ошибка: Несовпадение сигнатуры или версии или кода алгоритма")
            return

        decompressed_data = file.read()

    with open(output_file, 'wb') as file:
        file.write(decompressed_data)

def decode_format(input_file, output_file):
    with open(input_file, 'rb') as file:
        file_signature = file.read(len(signature))  # Замените на сигнатуру Л3.№1
        file_version = int.from_bytes(file.read(1), byteorder='big')
        file_algorithm_code = int.from_bytes(file.read(1), byteorder='big')
        compressed_data = file.read()

    if file_signature == signature_l1 and file_version == version_l1 and file_algorithm_code == 0:
        # Используем кодер Л1.№5 для декодирования
        decode_l1_format(input_file, output_file)
    else:
        # Используем кодер Л3.№1 для декодирования
        decode_huffman(input_file, output_file)

# Пример использования:
input_file = 'compressed.huffman_or_l1'  # Замените на путь к вашему сжатому файлу
output_file = 'decompressed.txt'  # Замените на имя файла для разжатых данных
decode_format(input_file, output_file)

