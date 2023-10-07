import pylzma

# Открываем файл для сжатия (замените "input.txt" на имя вашего файла)
input_file_path = "input.txt"
with open(input_file_path, "rb") as input_file:
    input_data = input_file.read()

# Сжимаем данные
compressed_data = pylzma.compress(input_data)

# Сохраняем сжатые данные в файл
compressed_file_path = "compressed.lzma"
with open(compressed_file_path, "wb") as compressed_file:
    compressed_file.write(compressed_data)

# Открываем сжатый файл и декомпрессируем данные
with open(compressed_file_path, "rb") as compressed_file:
    compressed_data = compressed_file.read()

# Декомпрессируем данные
decompressed_data = pylzma.decompress(compressed_data)

# Сравниваем длину сжатых данных с длиной исходных данных
print(f"Длина исходных данных: {len(input_data)} байт")
print(f"Длина сжатых данных: {len(compressed_data)} байт")

# Сравниваем с длиной данных, рассчитанной в Л2.№1
# (добавьте свой код из предыдущего ответа для расчета информации)

